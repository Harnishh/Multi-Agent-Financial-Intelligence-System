from tools.llm import llm

def risk_agent(state):

    company = state["company"]
    events = state["events"]

    prompt = f"""
You are an experienced Equity Research Analyst and Financial Risk Consultant.

Analyze the recent business events for the company: {company}.

Your objective is to identify ONLY risks that are supported by the provided events.
Do NOT invent risks or use outside knowledge.

Evaluate the company across the following dimensions:

1. Business Risk
   - Competition
   - Customer concentration
   - Strategic execution
   - Partnerships
   - Expansion risks

2. Financial Risk
   - Revenue uncertainty
   - Profitability concerns
   - Cash flow
   - Capital expenditure
   - Debt or liquidity concerns (only if mentioned)

3. Operational Risk
   - Supply chain
   - Workforce
   - Technology
   - Cybersecurity
   - Execution challenges

4. Market Risk
   - Industry trends
   - Macroeconomic factors
   - Regulatory issues
   - Investor sentiment
   - Stock volatility

For each category assign one level:

LOW
MEDIUM
HIGH

Then provide:

Overall Risk Score:
(integer from 0 to 100)

Risk Level:
LOW
MEDIUM
HIGH

Key Risks:
- Bullet points only

Risk Summary:
Explain in 5-8 concise sentences why the company received this risk score.

Important Rules:
- Base the analysis ONLY on the supplied events.
- If information is insufficient for a category, explicitly state:
  "Insufficient evidence."
- Be objective.
- Do not give investment advice.
- Do not recommend BUY or SELL.

Company:
{company}

Recent Events:
{events}
"""

    response = llm.invoke(prompt)

    return {
        "risk_analysis": response.text
    }