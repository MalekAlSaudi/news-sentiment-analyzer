import os

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
FIREBASE_KEY_PATH = os.environ.get("FIREBASE_KEY_PATH", "service-account.json")

if not NEWS_API_KEY:
    raise EnvironmentError("NEWS_API_KEY is not set.")
