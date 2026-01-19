# translation.py

from googletrans import Translator

# Initialize once
translator = Translator()


def translate_text(text: str, target_lang: str = "en") -> str:
    """
    Translate text into a target language.

    Args:
        text (str): Input text
        target_lang (str): Language code (e.g., 'fr', 'hi', 'es')

    Returns:
        str: Translated text
    """
    if not text.strip():
        return ""

    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"[Translation failed: {e}]"
