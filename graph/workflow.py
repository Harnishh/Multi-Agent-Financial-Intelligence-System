from langgraph.graph import StateGraph, START, END

from graph.state import FinancialState

from agents.supervisor import supervisor
from agents.ddgs_agent import ddgs_agent
from agents.rss_agent import rss_agent
from agents.news_aggregator_agent import news_aggregator_agent
from agents.filter_agent import filter_agent
from agents.event_extraction_agent import event_extraction_agent
from agents.risk_agent import risk_agent
from agents.sentiment_agent import sentiment_agent
from agents.report_agent import report_agent
from agents.yfinance_agent import yfinance_agent
from agents.prediction_agent import prediction_agent


def build_graph():

    builder = StateGraph(FinancialState)

    builder.add_node("supervisor", supervisor)
    builder.add_node("ddgs", ddgs_agent)
    builder.add_node("rss", rss_agent)
    builder.add_node("yfinance", yfinance_agent)
    builder.add_node("aggregator", news_aggregator_agent)
    builder.add_node("sentiment", sentiment_agent)
    builder.add_node("report", report_agent)
    builder.add_node("filter", filter_agent)
    builder.add_node("risk", risk_agent)
    builder.add_node("event", event_extraction_agent)
    builder.add_node("predictor", prediction_agent)

    builder.add_edge(START, "supervisor")

    builder.add_edge("supervisor", "ddgs")
    builder.add_edge("supervisor", "rss")
    builder.add_edge("supervisor", "yfinance")
    builder.add_edge("ddgs","aggregator")
    builder.add_edge("rss","aggregator")
    builder.add_edge("aggregator", "filter")
    builder.add_edge("filter", "event")
    builder.add_edge("event", "sentiment")
    builder.add_edge("sentiment", "risk")
    builder.add_edge("risk", "predictor")
    builder.add_edge("predictor", "report")


    builder.add_edge("report", END)

    return builder.compile()