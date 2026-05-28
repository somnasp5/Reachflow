
from app.core.runtime_state import logs


def portal_detector_agent(state):

    print("\n--- PORTAL DETECTOR AGENT RUNNING ---")

    logs.append("PORTAL DETECTOR AGENT RUNNING")

    html = state["html"].lower()

    portal = "unknown"

    logs.append("Detecting job portal from HTML")

    if "naukri" in html:

        portal = "naukri"

    elif "internshala" in html:

        portal = "internshala"

    elif "foundit" in html:

        portal = "foundit"

    print("DETECTED PORTAL:", portal)

    logs.append(f"Detected portal: {portal}")

    return {
        "portal": portal
    }
