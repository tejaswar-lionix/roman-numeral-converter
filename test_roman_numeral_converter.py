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


class AddRomanTests(unittest.TestCase):
    def test_add_roman(self):
        from roman import add_roman

        self.assertEqual(add_roman("X", "V"), "XV")
        self.assertEqual(add_roman("MCMXCIV", "VI"), "MM")

    def test_add_roman_rejects_large_sum(self):
        from roman import add_roman

        with self.assertRaises(ValueError):
            add_roman("MMM", "M")


class SubtractRomanTests(unittest.TestCase):
    def test_subtract_roman(self):
        from roman import subtract_roman

        self.assertEqual(subtract_roman("X", "V"), "V")
        self.assertEqual(subtract_roman("MCMXCIV", "VI"), "MCMLXXXVIII")

    def test_equal_numerals_raise(self):
        from roman import subtract_roman

        with self.assertRaises(ValueError):
            subtract_roman("X", "X")

    def test_larger_right_raises(self):
        from roman import subtract_roman

        with self.assertRaises(ValueError):
            subtract_roman("V", "X")


class SumRomanTests(unittest.TestCase):
    def test_sum_roman(self):
        from roman import sum_roman

        self.assertEqual(sum_roman(["X", "V"]), "XV")
        self.assertEqual(sum_roman(["MCMXCIV", "VI"]), "MM")

    def test_sum_roman_rejects_large_total(self):
        from roman import sum_roman

        with self.assertRaises(ValueError):
            sum_roman(["MMM", "M"])

    def test_sum_roman_rejects_empty(self):
        from roman import sum_roman

        with self.assertRaises(ValueError):
            sum_roman([])

    def test_sum_roman_propagates_invalid_numeral(self):
        from roman import sum_roman

        with self.assertRaises(ValueError):
            sum_roman(["X", "ABC"])


class CompareRomanTests(unittest.TestCase):
    def test_less_than(self):
        from roman import compare_roman

        self.assertEqual(compare_roman("IV", "V"), -1)

    def test_equal(self):
        from roman import compare_roman

        self.assertEqual(compare_roman("X", "x"), 0)

    def test_greater_than(self):
        from roman import compare_roman

        self.assertEqual(compare_roman("MCMXCIV", "VI"), 1)

    def test_invalid_numerals_propagate(self):
        from roman import compare_roman

        with self.assertRaises(ValueError):
            compare_roman("ABC", "I")
        with self.assertRaises(ValueError):
            compare_roman("I", "ABC")


if __name__ == "__main__":
    unittest.main()
