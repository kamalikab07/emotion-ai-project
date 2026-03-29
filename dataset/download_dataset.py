"""
Run this once: python dataset/download_dataset.py
Downloads the 'emotion' dataset from HuggingFace (~20k tweets, 6 emotions)
"""

import pandas as pd
import requests
import os

def download():
    print("📥 Downloading dataset...")

    url = "https://raw.githubusercontent.com/dair-ai/emotion_dataset/master/data/train.txt"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Download failed. Using fallback synthetic data.")
        create_fallback()
        return

    rows = []
    for line in response.text.strip().split("\n"):
        parts = line.strip().split(";")
        if len(parts) == 2:
            rows.append({"text": parts[0], "emotion": parts[1]})

    df = pd.DataFrame(rows)
    os.makedirs("dataset", exist_ok=True)
    df.to_csv("dataset/emotions.csv", index=False)
    print(f"✅ Dataset saved: {len(df)} rows, emotions: {df['emotion'].unique()}")


def create_fallback():
    data = {
        "text": [
            "I am so happy today", "This is the worst day ever",
            "I feel so angry right now", "I am excited for my trip",
            "I feel depressed and lonely", "Why is everything so frustrating",
            "Life is beautiful and amazing", "I am tired of everything",
            "This makes me so mad", "I feel great and joyful",
            "I am scared of what happens next", "Everything feels so overwhelming",
            "I love spending time with friends", "I hate Mondays so much",
            "Feeling nervous about my interview", "So grateful for everything I have"
        ],
        "emotion": [
            "joy", "sadness", "anger", "joy", "sadness", "anger",
            "joy", "sadness", "anger", "joy", "fear", "fear",
            "joy", "anger", "fear", "joy"
        ]
    }
    df = pd.DataFrame(data)
    df.to_csv("dataset/emotions.csv", index=False)
    print(f"✅ Fallback dataset created: {len(df)} rows")


if __name__ == "__main__":
    download()