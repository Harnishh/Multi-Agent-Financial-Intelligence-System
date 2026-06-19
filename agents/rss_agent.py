from tools.rss_tool import fetch_rss_news
def rss_agent(state):
    company = state["company"]
    news = fetch_rss_news(company)
    return{
        "rss_news": news
    }