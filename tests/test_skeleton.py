import inspect

import validkit

FUNCTIONS = {
    "is_valid_email": "validkit.email",
    "luhn_check": "validkit.luhn",
    "is_valid_iban": "validkit.iban",
    "is_valid_isbn13": "validkit.isbn",
    "normalize_phone": "validkit.phone",
    "strip_accents": "validkit.accents",
    "mask_secret": "validkit.mask",
    "slugify": "validkit.slug",
    "clamp": "validkit.clamp",
}

EXPECTED_SIGNATURES = {
    "is_valid_email": "(text: str) -> bool",
    "luhn_check": "(digits: str) -> bool",
    "is_valid_iban": "(text: str) -> bool",
    "is_valid_isbn13": "(text: str) -> bool",
    "normalize_phone": "(text: str, country_code: str | int) -> str",
    "strip_accents": "(text: str) -> str",
    "mask_secret": "(text: str, keep: int = 4) -> str",
    "slugify": "(text: str) -> str",
    "clamp": "(value: float, low: float, high: float) -> float",
}


def test_all_nine_functions_are_exported():
    for name in FUNCTIONS:
        assert hasattr(validkit, name), f"{name} is not exported from validkit"
        assert name in validkit.__all__, f"{name} is missing from validkit.__all__"


def test_each_function_lives_in_its_own_module():
    for name, module in FUNCTIONS.items():
        func = getattr(validkit, name)
        assert func.__module__ == module, (
            f"{name} is defined in {func.__module__}, expected {module}"
        )


def test_each_function_has_the_contract_signature():
    for name, expected in EXPECTED_SIGNATURES.items():
        func = getattr(validkit, name)
        assert callable(func), f"{name} is not callable"
        signature = str(inspect.signature(func))
        assert signature == expected, f"{name}: signature {signature!r} != {expected!r}"
