def build_prompt(emotion: str, confidence: dict, user_input: str) -> str:
    main_conf = confidence.get(emotion, 0)

    return f"""You are a creative AI storyteller. A user shared their feelings and you must write a short story inspired by them.

Detected emotion: {emotion} (confidence: {main_conf:.0%})
User said: "{user_input}"

Instructions:
- Write a short, engaging story (5–8 lines)
- Clearly reflect the emotion: {emotion}
- Make it vivid, cinematic, and human
- Do NOT mention the word "{emotion}" directly — show it through the story

Story:"""