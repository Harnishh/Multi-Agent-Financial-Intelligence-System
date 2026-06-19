import feedparser

def fetch_rss_news(company):
    feeds = [
        "https://www.moneycontrol.com/rss/business.xml",
        "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
    ]
    results = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            text = f"{entry.title} {entry.get('summary', '')}"
            if company.lower() in text.lower():
                results.append(
                    f"Title: {entry.title}\n"
                    f"Summary: {entry.get('summary', '')}\n"
                )

    return "\n".join(results[:10]) 