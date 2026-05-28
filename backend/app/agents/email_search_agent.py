
from app.services.company_search_service import (
    get_company_emails,
    get_company_info
)

from app.core.runtime_state import logs


def email_search_agent(state):

    print("\n--- EMAIL SEARCH AGENT RUNNING ---")

    logs.append("EMAIL SEARCH AGENT RUNNING")

    jobs = state["jobs"]

    companies = []

    logs.append(f"Found {len(jobs)} jobs to process")

    for index, job in enumerate(jobs):

        company_name = job["company_name"]

        job_title = job["job_title"]

        print(f"\nProcessing {company_name}")

        logs.append(
            f"[{index + 1}/{len(jobs)}] Searching emails for {company_name}"
        )

        found_emails = get_company_emails(company_name)

        logs.append(
            f"Found {len(found_emails)} emails for {company_name}"
        )

        logs.append(
            f"Researching company info for {company_name}"
        )

        company_info = get_company_info(company_name)

        companies.append({

            "company_name": company_name,

            "job_title": job_title,

            "emails": found_emails,

            "company_info": company_info
        })

        print("\nCOMPANY:", company_name)

        print("JOB:", job_title)

        print("EMAILS:", found_emails[:3])

        logs.append(
            f"Completed processing for {company_name}"
        )

    logs.append(
        f"EMAIL SEARCH AGENT COMPLETED | Total companies: {len(companies)}"
    )

    return {
        "companies": companies
    }
