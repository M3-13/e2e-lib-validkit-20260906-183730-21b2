import pytest

from validkit import strip_accents


def test_strip_accents_removes_diacritics():
    assert strip_accents("Über Café") == "Uber Cafe"


def test_strip_accents_handles_various_special_characters():
    assert strip_accents("café, naïve, résumé, Jalapeño") == "cafe, naive, resume, Jalapeno"


def test_strip_accents_leaves_plain_text_unchanged():
    assert strip_accents("plain ASCII text 123") == "plain ASCII text 123"


def test_strip_accents_handles_empty_string():
    assert strip_accents("") == ""


def test_strip_accents_raises_type_error_on_non_string():
    with pytest.raises(TypeError):
        strip_accents(123)
    with pytest.raises(TypeError):
        strip_accents(None)
    with pytest.raises(TypeError):
        strip_accents(["Über", "Café"])
