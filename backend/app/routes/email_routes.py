import os
import tempfile
import traceback
from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from app.graph.workflow import graph as app_graph
from app.models.state import GraphState

router = APIRouter()


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from PDF file."""
    try:
        import PyPDF2
        text = ""
        with open(file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        return text
    except ImportError:
        raise HTTPException(status_code=500, detail="PyPDF2 not installed. Cannot process PDF.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from DOCX file."""
    try:
        import docx
        doc = docx.Document(file_path)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        return "\n".join(text)
    except ImportError:
        raise HTTPException(status_code=500, detail="python-docx not installed. Cannot process DOCX.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing DOCX: {str(e)}")


def csv_to_html_table(csv_content: str) -> str:
    """Convert CSV string to a simple HTML table."""
    lines = csv_content.strip().splitlines()
    if not lines:
        return "<table></table>"
    # Assume first line is header
    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]
    html = "<table><thead><tr>"
    for th in header:
        html += f"<th>{th.strip()}</th>"
    html += "</tr></thead><tbody>"
    for row in rows:
        html += "<tr>"
        for cell in row:
            html += f"<td>{cell.strip()}</td>"
        html += "</tr>"
    html += "</tbody></table>"
    return html


@router.post("/send-email")
async def generate_emails_endpoint(
    file: UploadFile = File(...),
    resume: UploadFile = File(...),
    custom_prompt: str = Form(None),
):
    """
    Generate personalized outreach emails for companies found in the uploaded file.
    Expected file: HTML (from Naukri, Internshala, or Foundit) or CSV.
    Expected resume: PDF or DOCX.
    Optional: custom_prompt string.
    """
    try:
        # Read the main file (HTML or CSV)
        content = await file.read()
        content_str = content.decode("utf-8")

        # Determine file type and set portal accordingly
        filename = file.filename.lower()
        if filename.endswith(('.html', '.htm')):
            html_content = content_str
            portal = ""
        elif filename.endswith('.csv'):
            html_content = content_str  # keep raw CSV string
            portal = "csv"
        else:
            # Assume HTML if extension not recognized
            html_content = content_str
            portal = ""

        # Read and extract text from resume
        resume_content = await resume.read()
        resume_filename = resume.filename.lower()
        # Save to temporary file for processing
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(resume_filename)[1]) as tmp:
            tmp.write(resume_content)
            tmp_path = tmp.name

        try:
            if resume_filename.endswith('.pdf'):
                resume_text = extract_text_from_pdf(tmp_path)
            elif resume_filename.endswith('.docx') or resume_filename.endswith('.doc'):
                resume_text = extract_text_from_docx(tmp_path)
            else:
                # Assume plain text
                resume_text = resume_content.decode("utf-8")
        finally:
            os.unlink(tmp_path)

        # Prepare initial state
        initial_state: GraphState = {
            "html": html_content,
            "resume_text": resume_text,
            "custom_prompt": custom_prompt if custom_prompt is not None else "",
            # Initialize other required fields with empty defaults
            "portal": portal,
            "jobs": [],
            "companies": [],
            "researched_companies": [],
            "final_output": [],
            "resume_context": {},  # Will be filled by resume_parser agent
        }

        # Run the workflow
        final_state = app_graph.invoke(initial_state)

        # Extract the final output
        result = final_state.get("final_output", [])

        # Ensure each item has the required fields
        formatted_result = []
        for item in result:
            formatted_result.append({

                "company_name": item.get("company_name", ""),
                
                "job_title": item.get("job_title", ""),
                "company_email": item.get("company_email", ""),
                "generated_email": item.get("generated_email", ""),
            })

        return formatted_result

    except HTTPException:
        raise
    except Exception as e:
        # Log the error for debugging
        print(f"Error in generate_emails_endpoint: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")