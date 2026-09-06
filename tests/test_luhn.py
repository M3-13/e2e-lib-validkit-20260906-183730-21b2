import pytest

from validkit.luhn import luhn_check


def test_reference_value_is_valid():
    assert luhn_check("79927398713") is True


def test_invalid_sequence_is_rejected():
    assert luhn_check("79927398712") is False


def test_hyphenated_input():
    assert luhn_check("7992-7398-713") is True


def test_space_separated_input():
    assert luhn_check("7992 7398 713") is True


def test_non_digit_character_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("7992739a713")


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        luhn_check(79927398713)


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("")


def test_only_separators_raise_value_error():
    with pytest.raises(ValueError):
        luhn_check("  -  ")
