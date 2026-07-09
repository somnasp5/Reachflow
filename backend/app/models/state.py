from typing import TypedDict, List, Dict


class GraphState(TypedDict):

    html: str

    portal: str

    jobs: List[Dict]

    companies: List[Dict]

    researched_companies: List[Dict]

    final_output: List[Dict]

    resume_text: str

    resume_context: Dict

    custom_prompt: str