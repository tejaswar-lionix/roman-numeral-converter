import unittest

from roman import from_roman, to_roman


class RomanTests(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_rejects_out_of_range(self):
        for number in (0, -1, 4000):
            with self.assertRaises(ValueError):
                to_roman(number)

    def test_from_roman(self):
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("mcmxciv"), 1994)

    def test_from_roman_rejects_invalid(self):
        for text in ("", "IIII", "ABC", "VX"):
            with self.assertRaises(ValueError):
                from_roman(text)

    def test_roundtrip(self):
        for number in (1, 9, 42, 1987, 3999):
            self.assertEqual(from_roman(to_roman(number)), number)


if __name__ == "__main__":
    unittest.main()
