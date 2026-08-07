import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news():
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": "Pakistan",
        "apiKey": API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "I couldn't get the latest news."

    data = response.json()

    articles = data["articles"]

    if not articles:
        return "No news found."

    headlines = []

    for article in articles:
        headlines.append(article["title"])

    return headlines


if __name__ == "__main__":
    news = get_news()

    if isinstance(news, list):
        for i, headline in enumerate(news, 1):
            print(f"{i}. {headline}")
    else:
        print(news)