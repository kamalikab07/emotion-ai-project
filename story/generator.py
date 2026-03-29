import os
from groq import Groq
from dotenv import load_dotenv
from story.prompts import build_prompt
from utils.logger import logger

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_story(emotion: str, confidence: dict, user_input: str) -> str:
    try:
        prompt = build_prompt(emotion, confidence, user_input)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Groq error: {e}")
        return "Story generation failed. Please check your API key."