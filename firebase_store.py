import firebase_admin
from firebase_admin import credentials, firestore

def init_firestore(key_path):
    if not firebase_admin._apps:
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
    return firestore.client()

def store_articles_to_firestore(db, articles, collection_name="news_articles"):
    """
    Stores sentiment-labeled articles into Firestore.
    """
    collection_ref = db.collection(collection_name)

    for article in articles:
        doc_data = {
            "title": article["title"],
            "description": article["description"],
            "sentiment": article["sentiment"],
            "source": article["source"],
            "publishedAt": article["publishedAt"]
        }
        collection_ref.add(doc_data)

    print(f"Stored {len(articles)} articles to Firestore collection '{collection_name}'.")
