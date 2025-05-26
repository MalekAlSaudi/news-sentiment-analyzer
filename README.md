# News Sentiment Analyzer

This project is a cloud-based news aggregation and sentiment analysis system built using Python. It retrieves the latest headlines from NewsAPI, analyzes their sentiment using a pre-trained Transformer model, and stores the enriched articles in a Firebase Firestore database.

## Features

- Fetches top headlines from NewsAPI
- Analyzes sentiment using CardiffNLP's RoBERTa model via HuggingFace Transformers
- Stores sentiment-tagged articles in Firebase Firestore
- Designed to be containerized using Docker and deployed to Kubernetes

## Project Structure

- `main.py` - Entry point that coordinates the entire pipeline
- `news_fetcher.py` - Fetches and filters news articles from NewsAPI
- `sentiment.py` - Performs sentiment analysis using a transformer model
- `firebase_store.py` - Uploads processed articles to Firestore
- `config.py` - Loads environment variables or constants
- `requirements.txt` - Lists required Python dependencies
- `Dockerfile` - Container definition for building and deploying the app

## Setup Instructions

### Prerequisites

- Python 3.10+
- A NewsAPI key (https://newsapi.org)
- A Firebase Firestore project and service account key

### Installation and Execution

1. Clone or download the repository.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

Set environment variables:
export NEWS_API_KEY=your_newsapi_key
export FIREBASE_KEY_PATH=path/to/service-account.json

Run the application:
python main.py


This will:

Fetch news articles from NewsAPI

Analyze their sentiment

Upload results to Firestore


Docker Support
To build and run the app in Docker:

docker build -t news-sentiment-app .
docker run -e NEWS_API_KEY=your_api_key -v /path/to/service-account.json:/app/service-account.json news-s

License
This project is for academic purposes only.
