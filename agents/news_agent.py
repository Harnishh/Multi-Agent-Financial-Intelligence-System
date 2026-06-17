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

def news_agent(state):
    company = state["company"]
    query = f"{company} recent business news"
    news = search_web(query)
    return{
        "news": news
    }