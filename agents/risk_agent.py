from tools.llm import llm

def risk_agent(state):
    events = state["events"]
    company = state["company"]
    prompt = f"""
You are a senior financial risk analyst.

Analyze the following company {company} developments,

Identify:

1. Business Risks
2. Financial Risks
3. Operational Risks
4. Market Risks

Assign:

LOW
MEDEUM
HIGH

Return:

RISK SCORE: 0-100

KEY RISKS:

RISK LEVEL:

JUSTIFICATION:

Data:

{events}
"""
    response = llm.invoke(prompt)
    return{
        "risk_analysis": response.text
    }