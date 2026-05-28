
from fastapi import APIRouter
import threading

from app.graph.workflow import graph
from app.core.runtime_state import logs, latest_result

router = APIRouter()


def run_graph_process():

    try:

        logs.append("STARTING PLACEMENT AGENT")

        with open("sample.html", "r", encoding="utf-8") as f:

            html = f.read()

        logs.append("HTML LOADED")

        result = graph.invoke({

            "html": html,

            "portal": "",

            "jobs": [],

            "companies": [],

            "researched_companies": [],

            "final_output": []
        })

        latest_result.clear()

        latest_result.extend(
            result["final_output"]
        )

        logs.append("ALL TASKS COMPLETED")

    except Exception as e:

        print("ERROR:", str(e))

        logs.append(f"ERROR: {str(e)}")


@router.post("/run-placement-agent")
async def run_agent():

    logs.clear()

    latest_result.clear()

    # RUN IN BACKGROUND THREAD

    thread = threading.Thread(
        target=run_graph_process
    )

    thread.start()

    return {
        "success": True,
        "message": "Process started"
    }


@router.get("/logs")
def get_logs():

    return {
        "logs": logs
    }


@router.get("/results")
def get_results():

    return {
        "companies": latest_result
    }
