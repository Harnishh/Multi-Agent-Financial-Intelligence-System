from typing import TypedDict

class FinancialState(TypedDict):
    query: str
    company: str
    news: str
    events: list
    filtered_news: str
    risk_analysis: str
    sentiment: str
    report: str