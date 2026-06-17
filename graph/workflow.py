from langgraph.graph import StateGraph, START, END

from graph.state import FinancialState

from agents.supervisor import supervisor
from agents.news_agent import news_agent
from agents.filter_agent import filter_agent
from agents.event_extraction_agent import event_extraction_agent
from agents.risk_agent import risk_agent
from agents.sentiment_agent import sentiment_agent
from agents.report_agent import report_agent


def build_graph():

    builder = StateGraph(FinancialState)

    builder.add_node("supervisor", supervisor)
    builder.add_node("news", news_agent)
    builder.add_node("filter", filter_agent)
    builder.add_node("event_extraction", event_extraction_agent)
    builder.add_node("risk", risk_agent)
    builder.add_node("sentiment", sentiment_agent)
    builder.add_node("report", report_agent)

    builder.add_edge(START, "supervisor")

    builder.add_edge("supervisor", "news")

    builder.add_edge("news", "filter")

    builder.add_edge("filter", "event_extraction")

    builder.add_edge("event_extraction", "risk")

    builder.add_edge("risk", "sentiment")

    builder.add_edge("sentiment", "report")

    builder.add_edge("report", END)

    return builder.compile()