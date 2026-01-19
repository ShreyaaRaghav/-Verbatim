# text_to_speech.py

from gtts import gTTS
import tempfile
import os


def text_to_speech(text: str, lang: str = "en") -> str:
    """
    Convert text to speech and return audio file path.

    Args:
        text (str): Input text
        lang (str): Language code (e.g., 'en', 'hi', 'fr')

    Returns:
        str: Path to generated audio file (.mp3)
    """
    if not text.strip():
        return ""

    try:
        tts = gTTS(text=text, lang=lang)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        return temp_file.name

    except Exception as e:
        return ""
