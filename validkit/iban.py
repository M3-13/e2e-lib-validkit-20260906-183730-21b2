def is_valid_iban(text: str) -> bool:
    """Return True if ``text`` is a structurally valid IBAN.

    The ISO 13616 modulo-97 check is applied: whitespace is ignored, the four
    leading characters are moved to the end, letters are turned into numbers
    (A=10 .. Z=35) and the resulting integer must be congruent to 1 modulo 97.
    """
    if not isinstance(text, str):
        raise TypeError(f"is_valid_iban expects a str, got {type(text).__name__}")

    cleaned = "".join(text.split())
    if not cleaned.isalnum():
        return False

    cleaned = cleaned.upper()

    if len(cleaned) < 15 or len(cleaned) > 34:
        return False

    if not cleaned[:2].isalpha() or not cleaned[2:4].isdigit():
        return False

    rearranged = cleaned[4:] + cleaned[:4]

    digits = "".join(str(ord(ch) - ord("A") + 10) if ch.isalpha() else ch for ch in rearranged)

    return int(digits) % 97 == 1
