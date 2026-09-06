def clamp(value: float, low: float, high: float) -> float:
    for name, arg in (("value", value), ("low", low), ("high", high)):
        if isinstance(arg, bool) or not isinstance(arg, (int, float)):
            raise TypeError(f"clamp expects numeric arguments, got {type(arg).__name__} for {name}")

    if low > high:
        raise ValueError(f"low ({low}) must not be greater than high ({high})")

    return max(low, min(value, high))
