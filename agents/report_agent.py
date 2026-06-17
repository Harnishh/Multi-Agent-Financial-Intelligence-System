from tools.llm import llm

def report_agent(state):
    company = state["company"]
    filtered_news = state["filtered_news"]
    sentiment = state["sentiment"]
    risk_analysis = state["risk_analysis"]

    prompt = f"""
Create a financial report.

Company:
{company}

News:
{filtered_news}
 
Sentiment:
{sentiment}

Risk Analysis:
{risk_analysis}
"""
    response = llm.invoke(prompt)
    return {"report": response.text}