import time

import pytest

from validkit.phone import normalize_phone


def test_ac_example_without_country_code():
    assert normalize_phone("030 1234567", "49") == "+49301234567"


def test_ac_example_with_existing_country_code():
    assert normalize_phone("+49 30 1234567", "49") == "+49301234567"


def test_existing_plus_without_separators():
    assert normalize_phone("+49301234567", "49") == "+49301234567"


def test_int_country_code():
    assert normalize_phone("030 1234567", 49) == "+49301234567"


def test_str_country_code():
    assert normalize_phone("030 1234567", "49") == "+49301234567"


def test_hyphens_and_parentheses_removed():
    assert normalize_phone("(030) 123-45-67", "49") == "+49301234567"


def test_leading_zero_of_area_code_removed():
    assert normalize_phone("0301234567", 49) == "+49301234567"


def test_unknown_country_code_raises_valueerror():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "999")


def test_non_digit_country_code_raises_valueerror():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "DE")


def test_empty_number_raises_valueerror():
    with pytest.raises(ValueError):
        normalize_phone("", "49")
    with pytest.raises(ValueError):
        normalize_phone("   ", "49")
    with pytest.raises(ValueError):
        normalize_phone("+", "49")


def test_wrong_type_text_raises_typeerror():
    with pytest.raises(TypeError):
        normalize_phone(123, "49")
    with pytest.raises(TypeError):
        normalize_phone(None, "49")


def test_wrong_type_country_code_raises_typeerror():
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", 49.0)
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", None)


def test_long_input_terminates_quickly():
    long_text = "9" * 10000
    start = time.perf_counter()
    result = normalize_phone(long_text, "49")
    elapsed = time.perf_counter() - start
    assert result == "+49" + "9" * 10000
    assert elapsed < 1.0
