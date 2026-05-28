import pandas as pd

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)

from app.services.company_search_service import (
    get_company_info
)

from app.services.ollama_service import (
    generate_custom_email
)

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(

    file: UploadFile = File(...),

    custom_prompt: str = Form(...)
):

    df = pd.read_csv(file.file)

    final_output = []

    for _, row in df.iterrows():

        company_name = str(
            row.get("company_name", "")
        )

        hr_name = str(
            row.get("hr_name", "")
        )

        email = str(
            row.get("email", "")
        )

        position = str(
            row.get("position", "")
        )

        # COMPANY RESEARCH

        company_info = get_company_info(
            company_name
        )

        # GENERATE EMAIL

        generated_email = generate_custom_email(

            company_name=company_name,

            hr_name=hr_name,

            position=position,

            company_info=company_info,

            custom_prompt=custom_prompt
        )

        final_output.append({

            "company_name": company_name,

            "hr_name": hr_name,

            "company_email": email,

            "job_title": position,

            "generated_email": generated_email
        })

    return {
        "companies": final_output
    }
