"""
Email Generator Agent - Generates personalized outreach emails using LLM.
Updated to use retrieved context from RAG and resume context from parser.
"""

from app.services.ollama_service import generate_custom_email
from app.core.runtime_state import logs

def email_generator_agent(state):
    """
    Generates personalized outreach emails for each company.
    Expected state keys:
      - researched_companies: list of dicts with company_name, job_title, company_email,
                              retrieved_context, source_urls, last_updated
      - resume_context: dict with keys skills, projects, experience, education, certifications
    """
    print("\n--- EMAIL GENERATOR AGENT RUNNING ---")
    logs.append("EMAIL GENERATOR AGENT RUNNING")

    companies = state.get("researched_companies", [])
    resume_context = state.get("resume_context", {})

    # Prepare resume summary string
    def _format_resume(ctx):
        parts = []
        if ctx.get("skills"):
            skills = ", ".join(ctx["skills"][:10])  # limit to top 10
            parts.append(f"Skills: {skills}.")
        if ctx.get("projects"):
            proj_names = [p.get("name", "") for p in ctx["projects"] if isinstance(p, dict) and p.get("name")]
            proj_names = [n for n in proj_names if n]
            if proj_names:
                parts.append(f"Projects: {', '.join(proj_names[:5])}.")
        if ctx.get("experience"):
            exp_items = []
            for exp in ctx["experience"]:
                if isinstance(exp, dict):
                    role = exp.get("role", "")
                    company = exp.get("company", "")
                    if role or company:
                        exp_items.append(f"{role} at {company}".strip())
            if exp_items:
                parts.append(f"Experience: {', '.join(exp_items[:3])}.")
        if ctx.get("education"):
            edu = ctx["education"]
            if isinstance(edu, str) and edu.strip():
                parts.append(f"Education: {edu}.")
            elif isinstance(edu, dict):
                # e.g., {"degree": "B.Tech", "institution": "...", "year": "2026"}
                parts.append(f"Education: {edu.get('degree', '')} from {edu.get('institution', '')}.")
        if ctx.get("certifications"):
            certs = ", ".join(ctx["certifications"][:5])
            parts.append(f"Certifications: {certs}.")
        return " ".join(parts)

    resume_summary = _format_resume(resume_context)

    final_output = []

    for company in companies:
        company_name = company.get("company_name", "")
        job_title = company.get("job_title", "")
        company_email = company.get("company_email", "")
        retrieved_context = company.get("retrieved_context", "")

        if not company_name:
            continue

        logs.append(f"Generating email for {company_name}")

        # Build custom prompt that includes company and student context
        custom_prompt = f"""
You are the official Placement Coordination Team of IIIT Bhubaneswar writing a real placement outreach email to a company recruiter or hiring team.

Your goal is to professionally approach the company for internship, placement, and campus hiring opportunities for the 2026 graduating batch.

========================
COMPANY DETAILS
========================

Company Name:
{company_name}

Relevant Job Role:
{job_title}

Company Background (from recent research):
{retrieved_context if retrieved_context else "No specific details available."}

========================
STUDENT PROFILE
========================

The candidate(s) from IIIT Bhubaneswar have the following background:
{resume_summary if resume_summary else "Skills, projects, and experience as per resume."}

========================
COLLEGE DETAILS
========================

Institute:
International Institute of Information Technology (IIIT) Bhubaneswar

Graduating Batch:
2026

Eligible Branches:
- Computer Engineering (CE)
- Computer Science Engineering (CSE)
- Information Technology (IT)
- Electronics & Telecommunication (ETC)
- Electrical & Electronics Engineering (EEE)

========================
EMAIL OBJECTIVE
========================

Write a professional placement outreach email requesting the company to consider IIIT Bhubaneswar students for:
- internships
- full-time roles
- campus recruitment opportunities

========================
WRITING STYLE
========================

The email MUST:
- sound natural and human-written
- sound professional and confident
- feel personalized to the company
- reference the company domain/work naturally
- mention the relevant role naturally
- avoid sounding overly sales-like
- avoid robotic AI wording
- avoid generic template language
- avoid repetition
- avoid bullet points
- avoid placeholders
- avoid exaggerated claims

========================
IMPORTANT INSTRUCTIONS
========================

- Keep the email concise but impactful
- Keep tone formal and respectful
- Maximum length: 220 words
- Write in proper paragraphs
- Mention why IIIT Bhubaneswar students are suitable (refer to their skills/projects/experience)
- End with a polite call for further discussion or collaboration

========================
OUTPUT RULES
========================

Return ONLY the email body.

Do NOT generate:
- subject line
- greetings like "Dear Sir/Madam" repeatedly
- explanations
- notes
- markdown
- bullet points
"""

        try:
            generated_email = generate_custom_email(
                company_name=company_name,
                hr_name="",  # We don't have HR name; leave empty
                position=job_title,
                company_info="",  # Not used because we put all in custom_prompt
                custom_prompt=custom_prompt
            )
        except Exception as e:
            logs.append(f"Error generating email for {company_name}: {e}")
            generated_email = "Error generating email."

        final_output.append({
            "company_name": company_name,
            "job_title": job_title,
            "company_email": company_email,
            "generated_email": generated_email.strip()
        })

        print(f"EMAIL GENERATED FOR {company_name}")
        logs.append(f"Email generated successfully for {company_name}")

    logs.append(f"Generated emails for {len(final_output)} companies")
    return {
        "final_output": final_output
    }