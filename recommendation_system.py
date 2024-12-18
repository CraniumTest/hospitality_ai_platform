import pandas as pd

def make_recommendations(data_path):
    # Load data
    df = pd.read_csv(data_path)
    
    # Simple recommendation logic based on guest past interactions
    recommendations = []
    for _, row in df.iterrows():
        recommendations.append(f"Recommend {row['favorite_activity']} for {row['guest_name']}")
    
    return recommendations
