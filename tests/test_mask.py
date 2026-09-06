import pytest

from validkit.mask import mask_secret


def test_ac_example_keeps_last_four():
    assert mask_secret("geheim123456", keep=4) == "********3456"


def test_ac_example_full_mask_when_keep_zero():
    assert mask_secret("geheim", keep=0) == "******"


def test_keep_at_least_length_leaves_text_unchanged():
    assert mask_secret("geheim", keep=6) == "geheim"
    assert mask_secret("geheim", keep=100) == "geheim"


def test_default_keep_is_four():
    assert mask_secret("geheim") == "**heim"


def test_empty_text_returns_empty_string():
    assert mask_secret("", keep=0) == ""
    assert mask_secret("", keep=4) == ""


def test_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("geheim", keep=-1)


def test_wrong_text_type_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(123456, keep=4)


def test_wrong_keep_type_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("geheim", keep="4")
