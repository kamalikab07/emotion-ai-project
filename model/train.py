"""
Run this to train the model: python -m model.train
"""

import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from model.pipeline import create_pipeline
from utils.preprocess import clean_text
from utils.logger import logger


def train():
    logger.info("🚀 Training started...")

    # Load dataset
    csv_path = "dataset/emotions.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError("Dataset not found. Run: python dataset/download_dataset.py")

    df = pd.read_csv(csv_path)
    logger.info(f"✅ Loaded {len(df)} rows | Emotions: {df['emotion'].unique()}")

    # Clean text
    df["text"] = df["text"].apply(clean_text)
    df = df[df["text"].str.strip() != ""]  # drop empty rows

    X = df["text"]
    y = df["emotion"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train
    pipeline = create_pipeline()
    pipeline.fit(X_train, y_train)
    logger.info("✅ Model trained")

    # Evaluate
    y_pred = pipeline.predict(X_test)
    report = classification_report(y_test, y_pred)
    logger.info(f"\n📊 Classification Report:\n{report}")

    # Save
    os.makedirs("model", exist_ok=True)
    joblib.dump(pipeline, "model/saved_model.pkl")
    logger.info("✅ Model saved to model/saved_model.pkl")


if __name__ == "__main__":
    train()