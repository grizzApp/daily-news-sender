from app.news_fetcher import get_news
from app.utils import text_cleaner, email_sender
import asyncio

def start():
    data = asyncio.run(get_news())
    if not data or data.get("status") != "ok":
        print("Failed to fetch news.")
        return

    top_articles = data.get('articles', [])[:5]
    if not top_articles:
        print("No articles to send.")
        return

    new_top_articles = text_cleaner(top_articles)
    email_sender(new_top_articles)

if __name__ == "__main__":
    start()