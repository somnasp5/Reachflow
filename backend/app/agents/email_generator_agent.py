"""
Email Generator Agent - Generates personalized outreach emails.
"""

from app.services.ollama_service import generate_custom_email
from app.core.runtime_state import logs


def email_generator_agent(state):
    print("\n--- EMAIL GENERATOR AGENT RUNNING ---")
    logs.append("EMAIL GENERATOR AGENT RUNNING")

    companies = state.get("researched_companies", [])
    resume_context = state.get("resume_context", {})

    final_output = []

    for company in companies:
        company_name = company.get("company_name", "")
        job_title = company.get("job_title", "")
        company_email = company.get("company_email", "")
        retrieved_context = company.get("retrieved_context", "")
        print("\n========== EMAIL CONTEXT ==========")
        print(company_name)
        print(retrieved_context[:500])
        print("Context length:", len(retrieved_context))
        print("===================================\n")

        if not company_name:
            continue

        logs.append(f"Generating email for {company_name}")

        custom_prompt = f"""
Student Details:
- Name: {resume_context.get('name', '')}
- College: {resume_context.get('college', '')}
- Branch: {resume_context.get('branch', '')}
- Graduation Year: {resume_context.get('graduation_year', '')}
- Skills: {", ".join(resume_context.get("skills", []))}
- Projects: {", ".join(resume_context.get("projects", []))}
- Experience: {", ".join(resume_context.get("experience", []))}

Company Details:
- Company Name: {company_name}
- Job Role: {job_title}
- Company Context: {retrieved_context}

Write a personalized cold email from the student's perspective.

The first paragraph should briefly introduce the student.

The second paragraph should naturally connect the student's skills or projects with the company and the role.

The final paragraph should politely express interest in an internship, full-time, or campus opportunity and request a chance to connect.

Rules:
- 120-150 words only.
- Professional and natural.
- Mention only information available in the resume.
- Do not invent skills or projects.
- Do not praise the company excessively.
- Do not repeat ideas.
- No bullet points.
- Do not mention the placement cell.
- Return only the email body.
"""

        try:
            generated_email = generate_custom_email(
    company_name=company_name,
    hr_name="",
    position=job_title,
    company_info=retrieved_context,
    custom_prompt=custom_prompt,
)

            final_output.append({
                "company_name": company_name,
                "job_title": job_title,
                "company_email": company_email,
                "generated_email": generated_email.strip(),
            })

        except Exception as e:
            logs.append(f"Error generating email for {company_name}: {e}")

            fallback_email = (
                f"My name is {resume_context.get('name','')}. "
            )

            if resume_context.get("branch"):
                fallback_email += (
                    f"I am a {resume_context.get('branch')} student"
                )

            if resume_context.get("graduation_year"):
                fallback_email += (
                    f" graduating in {resume_context.get('graduation_year')}."
                )
            else:
                fallback_email += "."

            if resume_context.get("college"):
                fallback_email += (
                    f" I study at {resume_context.get('college')}."
                )

            fallback_email += (
                f" I am interested in opportunities at {company_name}"
            )

            if job_title:
                fallback_email += f" for the {job_title} role."

            fallback_email += (
                " I would appreciate the opportunity to discuss how my skills can contribute to your team."
                "\n\nBest regards,\n"
                + resume_context.get("name", "")
            )

            final_output.append({
                "company_name": company_name,
                "job_title": job_title,
                "company_email": company_email,
                "generated_email": fallback_email,
            })

    return {
        "final_output": final_output
    }