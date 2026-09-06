def luhn_check(digits: str) -> bool:
    """Validate a digit sequence with the Luhn algorithm.

    The input may contain spaces or hyphens as separators; they are ignored.
    From the right, every second digit is doubled and 9 is subtracted if the
    result exceeds 9. The sequence is valid if the total is divisible by 10.
    """
    if not isinstance(digits, str):
        raise TypeError(f"luhn_check() expects a str, got {type(digits).__name__}")

    cleaned = digits.replace(" ", "").replace("-", "")

    if not cleaned:
        raise ValueError("luhn_check() requires at least one digit")

    if not cleaned.isdigit():
        raise ValueError(
            "luhn_check() accepts only digits, optionally separated by spaces or hyphens, "
            f"got {digits!r}"
        )

    total = 0
    for index, char in enumerate(reversed(cleaned)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
