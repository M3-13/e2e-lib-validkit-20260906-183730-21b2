import time

import pytest

from validkit import is_valid_email


@pytest.mark.parametrize(
    "email",
    [
        "a@b.de",
        "user@example.com",
        "first.last@sub.example.co.uk",
        "user+tag@example.org",
        "user_name@example.io",
        "USER@EXAMPLE.COM",
        "john.doe123@mail.example.com",
    ],
)
def test_valid_emails(email: str) -> None:
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "a@b",
        "",
        "plainaddress",
        "@example.com",
        "user@",
        "user@example",
        "user@b.c",
        "user@example.123",
        "user@@example.com",
        "user@exam ple.com",
    ],
)
def test_invalid_emails(email: str) -> None:
    assert is_valid_email(email) is False


@pytest.mark.parametrize(
    "email",
    [
        "user @example.com",
        "user@ example.com",
        " user@example.com",
        "user@example.com ",
        "user@example.com\n",
        "user@exa\tmple.com",
    ],
)
def test_whitespace_rejected(email: str) -> None:
    assert is_valid_email(email) is False


@pytest.mark.parametrize(
    "value",
    [None, 123, 3.14, b"a@b.de", ["a@b.de"], {"email": "a@b.de"}],
)
def test_wrong_type_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        is_valid_email(value)


def test_long_input_terminates_quickly() -> None:
    long_input = "a" * 4999 + "@" + "b." * 2499 + "de"
    assert len(long_input) == 10_000
    start = time.perf_counter()
    is_valid_email(long_input)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.1
