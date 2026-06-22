from tools.yfinance_tool import get_company_data

def yfinance_agent(state):
    company = state["company"]
    company_data = get_company_data(company)
    return{"company_data": company_data}