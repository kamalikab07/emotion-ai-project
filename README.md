# 🎭 Emotion-Aware AI Story Generator

An end-to-end NLP project that detects emotions from text and generates creative stories using Google Gemini AI.

## Features
- 🔍 Emotion detection using TF-IDF + LinearSVC
- ✍️ AI story generation with Google Gemini
- ⚡ FastAPI REST backend
- 🎨 Gradio web interface

## Tech Stack
`Python` `scikit-learn` `FastAPI` `Gradio` `Google Gemini API`

## Setup

### 1. Clone the repo
git clone https://github.com/yourusername/emotion-ai-project.git
cd emotion-ai-project

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your API key
Create a `.env` file:
GEMINI_API_KEY=your_key_here

Get a free key at: https://makersuite.google.com/app/apikey

### 4. Download dataset & train model
python dataset/download_dataset.py
python -m model.train

### 5. Run the API
uvicorn api.main:app --reload

### 6. Run the UI (new terminal)
python app.py

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Status |
| POST | `/analyze` | Analyze text |

## Example API Request
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "I feel amazing today!"}'