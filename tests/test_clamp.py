import pytest

from validkit import clamp


def test_clamp_value_inside_range_is_unchanged():
    assert clamp(5, 0, 10) == 5


def test_clamp_value_below_range_is_raised_to_low():
    assert clamp(-3, 0, 10) == 0


def test_clamp_value_above_range_is_lowered_to_high():
    assert clamp(15, 0, 10) == 10


def test_clamp_lower_boundary():
    assert clamp(0, 0, 10) == 0


def test_clamp_upper_boundary():
    assert clamp(10, 0, 10) == 10


def test_clamp_with_float_values():
    assert clamp(2.5, 1.0, 3.0) == 2.5
    assert clamp(0.0, 1.0, 3.0) == 1.0
    assert clamp(4.0, 1.0, 3.0) == 3.0


def test_clamp_returns_a_number():
    result = clamp(7, 0, 10)
    assert isinstance(result, (int, float))


def test_clamp_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_clamp_non_numeric_value_raises_type_error():
    with pytest.raises(TypeError):
        clamp("5", 0, 10)
    with pytest.raises(TypeError):
        clamp(None, 0, 10)


def test_clamp_non_numeric_bounds_raise_type_error():
    with pytest.raises(TypeError):
        clamp(5, "0", 10)
    with pytest.raises(TypeError):
        clamp(5, 0, "10")
