def news_aggregator_agent(state):
    ddgs_news = state.get(
        "ddgs_news",
        ""
    )
    rss_news = state.get(
        "rss_news",
        ""
    )
    aggregated_news = f"""
=== DDGS NEWS ===
{ddgs_news}
=== RSS NEWS ===
{rss_news}
"""
    return{
        "aggregated_news": aggregated_news
    }