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
