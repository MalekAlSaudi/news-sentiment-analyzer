import requests

def fetch_top_headlines(api_key, country='us', page_size=10):
    """
    Fetches top news headlines using NewsAPI.
    """
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'apiKey': api_key,
        'country': country,
        'pageSize': page_size
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch news: {response.status_code} {response.text}")

    results = []
    for article in response.json().get('articles', []):
        results.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'source': article.get('source', {}).get('name'),
            'publishedAt': article.get('publishedAt')
        })

    return results
