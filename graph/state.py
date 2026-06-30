from typing import TypedDict

class FinancialState(TypedDict):
    query: str
    company: str
    ddgs_news: str
    rss_news: str
    aggregated_news: str
    filtered_news: str
    events: list
    company_data: dict
    risk_analysis: str
    sentiment: str
    ml_prediction: dict
    report: str