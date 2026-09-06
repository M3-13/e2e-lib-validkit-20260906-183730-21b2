import time

import pytest

from validkit import slugify


def test_slugify_removes_accents_and_lowercases():
    assert slugify("Über Café!") == "uber-cafe"


def test_slugify_collapses_multiple_hyphens():
    assert slugify("hello---world") == "hello-world"


def test_slugify_strips_leading_and_trailing_special_characters():
    assert slugify("!!!Hello World!!!") == "hello-world"


def test_slugify_lowercases_uppercase_input():
    assert slugify("HELLO WORLD") == "hello-world"


def test_slugify_handles_empty_string():
    assert slugify("") == ""


def test_slugify_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        slugify(123)
    with pytest.raises(TypeError):
        slugify(None)
    with pytest.raises(TypeError):
        slugify(["Über", "Café"])


def test_slugify_handles_ten_thousand_characters_under_100_ms():
    text = "a" * 10000
    start = time.perf_counter()
    slugify(text)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.1
