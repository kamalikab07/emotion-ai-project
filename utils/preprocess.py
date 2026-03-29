import re

def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'http\S+', '', text)        # remove URLs
    text = re.sub(r'@\w+', '', text)           # remove mentions
    text = re.sub(r'#\w+', '', text)           # remove hashtags
    text = re.sub(r'[^a-zA-Z\s]', '', text)   # remove special chars
    text = re.sub(r'\s+', ' ', text)           # remove extra spaces
    return text