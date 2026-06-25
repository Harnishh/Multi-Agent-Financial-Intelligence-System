from tools.llm import llm

def sentiment_agent(state):
    company = state["company"]
    news = state["filtered_news"]

    prompt = f"""
Analze sentimetn.

Company:
{company}

News:
{news}

Return:

Overall Sentimetn:
Reason: 
"""
    response = llm.invoke(prompt)
    return{
        "sentiment": response.text
    }