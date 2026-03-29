from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model.predict import predict_emotion
from story.generator import generate_story

app = FastAPI(
    title="Emotion AI API",
    description="Detects emotion from text and generates an AI story",
    version="1.0.0"
)


class TextInput(BaseModel):
    text: str


class EmotionResponse(BaseModel):
    emotion: str
    confidence: dict
    story: str


@app.get("/")
def root():
    return {"message": "Emotion AI API is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=EmotionResponse)
def analyze(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    emotion, confidence = predict_emotion(input.text)
    story = generate_story(emotion, confidence, input.text)

    return EmotionResponse(
        emotion=emotion,
        confidence=confidence,
        story=story
    )