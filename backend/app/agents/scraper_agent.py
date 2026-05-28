
from app.services.parsers.naukri_parser import parse_naukri_jobs
from app.services.parsers.internshala_parser import parse_internshala
from app.services.parsers.foundit_parser import parse_foundit

from app.core.runtime_state import logs


def scraper_agent(state):

    print("\n--- SCRAPER AGENT RUNNING ---")

    logs.append("SCRAPER AGENT RUNNING")

    portal = state["portal"]
    html = state["html"]

    jobs = []

    logs.append(f"Using parser for portal: {portal}")

    if portal == "naukri":

        logs.append("Parsing Naukri HTML")

        jobs = parse_naukri_jobs(html)

    elif portal == "internshala":

        logs.append("Parsing Internshala HTML")

        jobs = parse_internshala(html)

    elif portal == "foundit":

        logs.append("Parsing Foundit HTML")

        jobs = parse_foundit(html)

    else:

        logs.append("Unknown portal detected")

    print("\nTOTAL JOBS FOUND:", len(jobs))

    logs.append(f"Total jobs extracted: {len(jobs)}")

    for index, job in enumerate(jobs[:5]):

        company = job.get("company_name", "Unknown Company")

        role = job.get("job_title", "Unknown Role")

        logs.append(
            f"Job {index + 1}: {company} | {role}"
        )

    print(jobs[:3])

    logs.append("SCRAPER AGENT COMPLETED")

    return {
        "jobs": jobs
    }
