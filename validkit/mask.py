def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    if not isinstance(keep, int):
        raise TypeError(f"keep must be int, got {type(keep).__name__}")
    if keep < 0:
        raise ValueError(f"keep must be >= 0, got {keep}")

    length = len(text)
    if keep >= length:
        return text
    return "*" * (length - keep) + text[length - keep :]
