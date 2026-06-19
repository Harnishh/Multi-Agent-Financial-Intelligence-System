from tools.llm import llm

def filter_agent(state):
    news = state["aggregated_news"]
    prompt = f"""
You are a financial news analyst.

Below are raw search results.

Your job:

1. Remove duplicate information.
2. Ignore navigation pages.
3. Ignore investor relation pages.
4. Ignore generic company profile pages.
5. Extract only important business events.

Return:

KEY EVENTS:
- Event
- Impact

IMPORTANT SIGNALS:
- Positive
- Negative

RAW NEWS:

{news}
"""
    resoponse = llm.invoke(prompt)
    return{
        "filtered_news": resoponse.text
    }