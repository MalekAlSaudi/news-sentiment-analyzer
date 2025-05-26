from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

label_map = {
    'label_0': 'negative',
    'label_1': 'neutral',
    'label_2': 'positive'
}

def analyze_sentiment(text_list):
    predictions = sentiment_pipeline(text_list)
    results = []

    for text, pred in zip(text_list, predictions):
        readable_label = label_map.get(pred['label'].lower(), 'unknown')
        results.append({
            "text": text,
            "label": readable_label,
            "score": round(pred["score"], 4)
        })

    return results
