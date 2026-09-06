import re

from validkit.accents import strip_accents


def slugify(text: str) -> str:
    """Turn ``text`` into a URL-safe slug.

    Lowercases the input, strips accents, replaces every run of characters that
    are not ASCII letters or digits with a single hyphen, and removes any
    leading or trailing hyphens.
    """
    if not isinstance(text, str):
        raise TypeError(f"slugify() expects a str, got {type(text).__name__}")

    slug = strip_accents(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")
