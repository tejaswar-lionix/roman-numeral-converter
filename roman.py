#!/usr/bin/env python3
"""Convert between integers and Roman numerals."""
PAIRS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("number must be between 1 and 3999")
    remaining = number
    parts = []
    for value, symbol in PAIRS:
        count, remaining = divmod(remaining, value)
        parts.append(symbol * count)
    return "".join(parts)


def from_roman(text):
    if not text:
        raise ValueError("roman numeral must not be empty")
    cleaned = text.upper()
    index = 0
    total = 0
    for value, symbol in PAIRS:
        while cleaned.startswith(symbol, index):
            total += value
            index += len(symbol)
    if index != len(cleaned) or to_roman(total) != cleaned:
        raise ValueError(f"invalid roman numeral: {text}")
    return total


def add_roman(left, right):
    """Add two Roman numerals and return the Roman numeral sum."""
    total = from_roman(left) + from_roman(right)
    if total > 3999:
        raise ValueError("sum exceeds 3999")
    return to_roman(total)


def subtract_roman(left, right):
    """Subtract right from left and return the Roman numeral difference."""
    difference = from_roman(left) - from_roman(right)
    if difference <= 0:
        raise ValueError("difference must be positive")
    return to_roman(difference)


def sum_roman(values):
    """Sum an iterable of Roman numerals and return the Roman numeral total."""
    total = 0
    seen = False
    for value in values:
        seen = True
        total += from_roman(value)
    if not seen:
        raise ValueError("values must not be empty")
    if total > 3999:
        raise ValueError("sum exceeds 3999")
    return to_roman(total)


def compare_roman(left, right):
    """Compare two Roman numerals by value, returning -1, 0, or 1."""
    left_value = from_roman(left)
    right_value = from_roman(right)
    if left_value < right_value:
        return -1
    if left_value > right_value:
        return 1
    return 0
