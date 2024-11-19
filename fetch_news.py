import os, config
import requests
from datetime import datetime
from bs4 import BeautifulSoup

api_key = config.POLYGON_API_KEY
os.environ['POLYGON_API_KEY'] = api_key

symbols = ['GOOG', 'NVDA', 'AAPL', 'MSFT']
base_url = 'https://api.polygon.io/v2/reference/news'


def fetch_article_content(article_url):
    if article_url:
        response = requests.get(article_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract the body content
            body = soup.find('body')
            if body:
                return body.get_text()
    return ''


# Fetch news articles for each symbol
for symbol in symbols:
    # Define parameters for the API request
    params = {
        'ticker': symbol,
        'apiKey': api_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json().get('results', [])

        for article in news_data:
            # Extract relevant information from the article
            article_date = datetime.strptime(article['published_utc'], '%Y-%m-%dT%H:%M:%SZ').date()
            article_id = article['id']
            article_url = article.get('article_url', '')

            # Fetch the content of the article
            article_text = fetch_article_content(article_url)

            # Create a unique filename for each article using the ID
            article_filename = f"articles/{article_date}-{symbol}-{article_id}.html"

            # Save the article content to a file
            with open(article_filename, 'w', encoding='utf-8') as f:
                f.write(article_text)

            print(f"Saved article: {article_id}")
    else:
        # prints if message if news is unavailable 
        print(f"Failed to fetch news for {symbol}. Status code: {response.status_code}")

