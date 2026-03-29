import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/analyze"

EMOTION_EMOJI = {
    "joy": "😄", "sadness": "😢", "anger": "😠",
    "fear": "😨", "love": "❤️", "surprise": "😲"
}

def analyze(text: str):
    if not text.strip():
        return "Please enter some text.", {}, ""

    try:
        response = requests.post(API_URL, json={"text": text}, timeout=30)
        response.raise_for_status()
        data = response.json()

        emotion = data["emotion"]
        emoji = EMOTION_EMOJI.get(emotion, "🤔")
        label = f"{emoji} {emotion.capitalize()}"

        return label, data["confidence"], data["story"]

    except requests.exceptions.ConnectionError:
        return "❌ API not running. Start it with: uvicorn api.main:app --reload", {}, ""
    except Exception as e:
        return f"❌ Error: {str(e)}", {}, ""


with gr.Blocks(theme=gr.themes.Soft(), title="Emotion AI") as demo:
    gr.Markdown("# 🎭 Emotion-Aware AI Story Generator")
    gr.Markdown("Type how you feel — the AI detects your emotion and writes a story for you.")

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                lines=4,
                placeholder="e.g. I feel really anxious about my exams...",
                label="Your Text"
            )
            submit_btn = gr.Button("Analyze & Generate Story", variant="primary")

        with gr.Column():
            emotion_out = gr.Textbox(label="Detected Emotion")
            confidence_out = gr.JSON(label="Confidence Scores")

    story_out = gr.Textbox(label="AI Generated Story", lines=8)

    submit_btn.click(
        fn=analyze,
        inputs=text_input,
        outputs=[emotion_out, confidence_out, story_out]
    )

demo.launch()