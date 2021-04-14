import unittest

from string_calculator import StringCalculator


class TestPartOne(unittest.TestCase):

    def test_add(self):
        self.assertEqual(StringCalculator.add_list([19, 2, 37]), 58)

    def test_add_empty_list(self):
        self.assertEqual(StringCalculator.add_list([]), 0)

    def test_single_input(self):
        self.assertEqual(StringCalculator.add_list([1]), 1)

    def test_parse_input_with_comma(self):
        self.assertEqual(StringCalculator.parse_input("1,56,78"), [1, 56, 78])

    def test_parse_input_empty_string(self):
        self.assertEqual(StringCalculator.parse_input(""), [])

    def test_parse_input_single_input(self):
        self.assertEqual(StringCalculator.parse_input("1"), [1])

    def test_parse_input_single_input_with_newline_prefix(self):
        self.assertEqual(StringCalculator.parse_input("\n1"), [1])

    def test_parse_input_single_input_with_newline_suffix(self):
        self.assertEqual(StringCalculator.parse_input("1\n"), [1])

    def test_parse_input_with_newline_and_comma(self):
        self.assertEqual(StringCalculator.parse_input("1,\n2,3"), [1, 2, 3])
