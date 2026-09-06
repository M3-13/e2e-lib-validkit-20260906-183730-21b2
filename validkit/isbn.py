def is_valid_isbn13(text: str) -> bool:
    """Return True if *text* is a valid ISBN-13 (EAN-13) number.

    Hyphens and spaces are ignored. The remaining 13 digits (including the
    check digit) are validated by the EAN-13 weighted sum with alternating
    factors 1 and 3: the total must be divisible by 10.
    """
    if not isinstance(text, str):
        raise TypeError(f"is_valid_isbn13() expects a str, got {type(text).__name__}")

    cleaned = text.replace("-", "").replace(" ", "")
    if len(cleaned) != 13 or any(c not in "0123456789" for c in cleaned):
        return False

    total = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(cleaned))
    return total % 10 == 0
