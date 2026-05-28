
from app.services.ollama_service import generate_email
from app.core.runtime_state import logs


def email_generator_agent(state):

    print("\n--- EMAIL GENERATOR AGENT RUNNING ---")

    logs.append("EMAIL GENERATOR AGENT RUNNING")

    companies = state["researched_companies"]

    final_output = []

    for company in companies:

        company_name = company["company_name"]

        logs.append(
            f"Generating email for {company_name}"
        )

        generated_email = generate_email(

            company_name=company["company_name"],

            job_title=company["job_title"],

            company_info=company["company_info"]
        )

        final_output.append({

            "company_name": company["company_name"],

            "job_title": company["job_title"],

            "company_email": company["company_email"],

            "generated_email": generated_email
        })

        print(
            f"EMAIL GENERATED FOR {company_name}"
        )

        logs.append(
            f"Email generated successfully for {company_name}"
        )

    logs.append(
        f"Generated emails for {len(final_output)} companies"
    )

    return {
        "final_output": final_output
    }
