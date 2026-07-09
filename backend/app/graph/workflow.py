from langgraph.graph import StateGraph, END

from IPython.display import Image, display

from app.models.state import GraphState

from app.agents.portal_detector_agent import portal_detector_agent
from app.agents.scraper_agent import scraper_agent
from app.agents.email_search_agent import email_search_agent
from app.agents.email_filter_agent import email_filter_agent
from app.agents.company_research_agent import company_research_agent
from app.agents.email_generator_agent import email_generator_agent
from app.agents.resume_parser_agent import resume_parser_agent


builder = StateGraph(GraphState)

builder.add_node("portal_detector", portal_detector_agent)

builder.add_node("scraper", scraper_agent)

builder.add_node("email_search", email_search_agent)

builder.add_node("email_filter", email_filter_agent)

builder.add_node("company_research", company_research_agent)

builder.add_node("resume_parser", resume_parser_agent)

builder.add_node("email_generator", email_generator_agent)

builder.set_entry_point("portal_detector")

builder.add_edge("portal_detector", "scraper")

builder.add_edge("scraper", "email_search")

builder.add_edge("email_search", "email_filter")

builder.add_edge("email_filter", "company_research")

builder.add_edge("company_research", "resume_parser")

builder.add_edge("resume_parser", "email_generator")

builder.add_edge("email_generator", END)

graph = builder.compile()


try:

    display(

        Image(

            graph.get_graph().draw_mermaid_png()

        )

    )

except Exception as e:

    print("GRAPH VISUALIZATION ERROR:", e)