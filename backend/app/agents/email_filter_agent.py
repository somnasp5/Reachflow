
from app.core.runtime_state import logs


def email_filter_agent(state):

    print("\n--- EMAIL FILTER AGENT RUNNING ---")

    logs.append("EMAIL FILTER AGENT RUNNING")

    companies = state["companies"]

    filtered_companies = []

    for company in companies:

        company_name = company["company_name"]

        logs.append(
            f"Filtering emails for {company_name}"
        )

        emails = company["emails"]

        best_email = None

        if len(emails) > 0:

            best_email = emails[0]

            logs.append(
                f"Selected: {best_email}"
            )

        else:

            logs.append(
                f"No valid email found for {company_name}"
            )

        filtered_companies.append({

            "company_name": company["company_name"],

            "job_title": company["job_title"],

            "company_info": company["company_info"],

            "company_email": best_email
        })

        print(
            f"{company['company_name']} -> {best_email}"
        )

    logs.append(
        f"Filtered {len(filtered_companies)} companies"
    )

    return {
        "researched_companies": filtered_companies
    }
