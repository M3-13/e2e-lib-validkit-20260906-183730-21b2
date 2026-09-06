import pytest

from validkit import is_valid_isbn13


def test_valid_isbn13_with_hyphens():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_without_separators():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_isbn13_with_wrong_check_digit():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_isbn13_with_wrong_length():
    assert is_valid_isbn13("978-3-16-148410") is False
    assert is_valid_isbn13("978-3-16-148410-00") is False


def test_isbn13_with_non_digit_characters():
    assert is_valid_isbn13("978-3-16-14841x-0") is False


def test_isbn13_empty_string():
    assert is_valid_isbn13("") is False


def test_isbn13_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(9783161484100)  # type: ignore[arg-type]


def test_isbn13_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)  # type: ignore[arg-type]


def test_large_input_terminates_quickly():
    is_valid_isbn13("9" * 10_000)
