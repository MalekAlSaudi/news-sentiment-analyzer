from config import NEWS_API_KEY, FIREBASE_KEY_PATH
from news_fetcher import fetch_top_headlines
from sentiment import analyze_sentiment
from firebase_store import init_firestore, store_articles_to_firestore

def main():
    print("Fetching top headlines...")
    articles = fetch_top_headlines(NEWS_API_KEY)

    filtered = [a for a in articles if a.get('description')]
    descriptions = [a['description'] for a in filtered]

    print("Running sentiment analysis...")
    sentiments = analyze_sentiment(descriptions)

    for article, sentiment in zip(filtered, sentiments):
        article['sentiment'] = sentiment['label']

    print("Uploading to Firestore...")
    db = init_firestore(FIREBASE_KEY_PATH)
    store_articles_to_firestore(db, filtered, "news_articles_sentiment")

    print(f"Uploaded {len(filtered)} articles with sentiment labels.")

if __name__ == "__main__":
    main()
