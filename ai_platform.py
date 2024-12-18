from recommendation_system import make_recommendations
from sentiment_analysis import analyze_sentiments

def main():
    # Load guest preferences data (simplified for prototype)
    guest_data = "data/guest_preferences.csv"
    
    # Get personalized recommendations
    recommendations = make_recommendations(guest_data)
    print("Personalized Recommendations:")
    for rec in recommendations:
        print(rec)

    # Load sentiment analysis data (simplified for prototype)
    sentiment_data = "data/sentiment_data.csv"
    
    # Analyze sentiments
    sentiment_results = analyze_sentiments(sentiment_data)
    print("\nSentiment Analysis Results:")
    for result in sentiment_results:
        print(result)

if __name__ == "__main__":
    main()
