import pandas as pd
from textblob import TextBlob

def analyze_sentiments(data_path):
    # Load data
    df = pd.read_csv(data_path)
    
    # Analyze sentiments
    results = []
    for _, row in df.iterrows():
        blob = TextBlob(row['review'])
        sentiment = blob.sentiment.polarity
        sentiment_type = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"
        results.append(f"Review: {row['review']} is {sentiment_type}")
    
    return results
