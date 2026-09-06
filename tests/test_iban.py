import pytest

from validkit.iban import is_valid_iban

GERMAN_IBAN = "DE89 3704 0044 0532 0130 00"


def test_german_example_iban_is_valid():
    assert is_valid_iban(GERMAN_IBAN) is True


def test_wrong_check_digit_is_invalid():
    assert is_valid_iban("DE88 3704 0044 0532 0130 00") is False


def test_iban_without_spaces_is_valid():
    assert is_valid_iban("DE89370400440532013000") is True


def test_iban_with_varying_whitespace_is_valid():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True
    assert is_valid_iban("DE89\t3704 0044 0532 0130 00") is True
    assert is_valid_iban("  DE89 3704 0044 0532 0130 00  ") is True


def test_lowercase_iban_is_valid():
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_invalid_length_is_false():
    assert is_valid_iban("DE89 3704") is False
    assert is_valid_iban("") is False
    assert is_valid_iban("DE893704004405320130001234567890") is False


def test_invalid_characters_are_false():
    assert is_valid_iban("DE89-3704-0044-0532-0130-00") is False
    assert is_valid_iban("DE89 3704 0044 0532 0130 O0") is False


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(12345)
    with pytest.raises(TypeError):
        is_valid_iban(None)
    with pytest.raises(TypeError):
        is_valid_iban(["DE89 3704 0044 0532 0130 00"])


def test_long_input_terminates_and_is_false():
    assert is_valid_iban("X" * 10000) is False
