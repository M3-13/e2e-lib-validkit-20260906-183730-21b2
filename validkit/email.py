import re

_EMAIL_RE = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def is_valid_email(text: str) -> bool:
    """Return True if *text* is a pragmatically valid email address.

    Checks a ``local@domain`` shape: the local part uses common allowed
    characters, the domain contains at least one dot and ends in an
    alphabetic top-level domain of at least two characters. Whitespace is
    rejected and there must be exactly one ``@``.
    """
    if not isinstance(text, str):
        raise TypeError(f"is_valid_email() argument must be a str, not {type(text).__name__}")
    return _EMAIL_RE.fullmatch(text) is not None
