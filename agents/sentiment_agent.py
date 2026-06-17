from tools.llm import llm

def sentiment_agent(state):
    news = state["filtered_news"]

    prompt = f"""
Analze sentimetn.

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