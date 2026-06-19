from ddgs import DDGS

def search_web(query):
    with DDGS() as ddgs:
        results = ddgs.text(
            query,
            max_results = 5
        )
        output = []
        for r in results:
            output.append(
                f"""
                Title: {r['title']}
                Body: {r['body']}
                """
            )
        return "\n".join(output)

def ddgs_agent(state):
    company = state["company"]
    query = (f"{company} latest earnings"
              f"AI partnerships acqisitions"
              f"market developments")
    news = search_web(query)
    return{
        "ddgs_news": news
    }