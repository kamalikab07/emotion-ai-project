import joblib
import os
from scipy.special import softmax
from utils.preprocess import clean_text
from utils.logger import logger

_model = None

def load_model():
    global _model
    if _model is None:
        model_path = "model/saved_model.pkl"
        if not os.path.exists(model_path):
            raise FileNotFoundError("Model not found. Run: python -m model.train")
        _model = joblib.load(model_path)
        logger.info("✅ Model loaded")
    return _model


def predict_emotion(text: str) -> tuple[str, dict]:
    model = load_model()
    cleaned = clean_text(text)

    prediction = model.predict([cleaned])[0]
    scores = model.decision_function([cleaned])[0]
    classes = model.classes_
    probs = softmax(scores)

    confidence = {
        classes[i]: round(float(probs[i]), 3)
        for i in range(len(classes))
    }

    return prediction, confidence