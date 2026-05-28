
from app.core.runtime_state import logs


def company_research_agent(state):

    print("\n--- COMPANY RESEARCH AGENT RUNNING ---")

    logs.append("COMPANY RESEARCH AGENT RUNNING")

    researched_companies = state["researched_companies"]

    logs.append(
        f"Researched {len(researched_companies)} companies"
    )

    return {
        "researched_companies": researched_companies
    }

