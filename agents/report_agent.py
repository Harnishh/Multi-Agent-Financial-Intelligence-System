from tools.llm import llm

def report_agent(state):
    company = state["company"]
    company_data = state.get(
        "company_data",
        {}
    )
    filtered_news = state["filtered_news"]
    events = state.get(
        "events",
        []
    )
    sentiment = state["sentiment"]
    risk_analysis = state["risk_analysis"]

    prompt = f"""
You are a professional financial analyst.

Generate a detailed financial intelligence report.

Structure the report with the following section:

1. Executive Summary

2. Company Snapshot
    - Company Name
    - Sector
    - Industry
    - Currect Price
    - Market Cap
    - PE Ratio
    - 52 Week High
    - 52 Week Low

3. Key Business Events

4. Risk Assessment

5. Market Sentiment

6. Investment Outlook

Company:
{company}

Company Data:
{company_data}

Extracted Events:
{events}

News:
{filtered_news}

Sentiment:
{sentiment}

Risk Analysis:
{risk_analysis}

Write the report in a professional equity research style.
Use markdown formatting
"""
    response = llm.invoke(prompt)
    return {"report": response.text}