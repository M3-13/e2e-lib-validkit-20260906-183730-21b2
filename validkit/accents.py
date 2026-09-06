import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"strip_accents expects str, got {type(text).__name__}")

    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if not unicodedata.combining(char))
