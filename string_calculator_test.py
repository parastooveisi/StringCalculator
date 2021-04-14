import unittest

from string_calculator import StringCalculator


class TestPartOne(unittest.TestCase):

    def test_add_comma_delimiter(self):
        self.assertEqual(StringCalculator().add("1,2,3"), 6)

    def test_add_empty_input(self):
        self.assertEqual(StringCalculator().add(""), 0)

    def test_add_comma_delimiter_with_new_line(self):
        self.assertEqual(StringCalculator().add("\n10, 3, 5"), 18)

    def test_add_custom_delimiter(self):
        self.assertEqual(StringCalculator().add("//%\n1%3%4"), 8)

    def test_add_negative_inputs(self):
        self.assertRaises(Exception, StringCalculator(
        ).handle_negative_numbers, "1, -4, 5, -7")

    def test_add_large_numbers_bonus_one(self):
        self.assertEqual(StringCalculator().add("1000,2000,3"), 3)

    def test_add_delimiters_arbitrary_length_bonus_two(self):
        self.assertEqual(StringCalculator().add("//$$\n1$$20$$3000"), 21)

    def test_add_multiple_delimiters_bonus_three(self):
        self.assertEqual(StringCalculator().add("//$,@,*\n1$2@3*6"), 12)

    def test_add_multiple_delimiters_arbitrary_length_bonus_four(self):
        self.assertEqual(StringCalculator().add("//$$,@\n1$$20@3000"), 21)

    def test_add_list(self):
        self.assertEqual(StringCalculator().add_list([19, 2, 37]), 58)

    def test_add_large_number(self):
        self.assertEqual(StringCalculator().add_list([19, 2, 1000]), 21)

    def test_add_empty_list(self):
        self.assertEqual(StringCalculator().add_list([]), 0)

    def test_single_input(self):
        self.assertEqual(StringCalculator().add_list([1]), 1)

    def test_parse_input_with_comma(self):
        self.assertEqual(StringCalculator().parse_input(
            "1,56,78"), [1, 56, 78])

    def test_parse_input_empty_string(self):
        self.assertEqual(StringCalculator().parse_input(""), [])

    def test_parse_input_single_input(self):
        self.assertEqual(StringCalculator().parse_input("1"), [1])

    def test_parse_input_single_input_with_newline_prefix(self):
        self.assertEqual(StringCalculator().parse_input("\n1"), [1])

    def test_parse_input_single_input_with_newline_suffix(self):
        self.assertEqual(StringCalculator().parse_input("1\n"), [1])

    def test_parse_input_with_newline_and_comma(self):
        self.assertEqual(StringCalculator().parse_input("1,\n2,3"), [1, 2, 3])

    def test_parse_input_with_multiple_delimiters(self):
        self.assertEqual(StringCalculator().parse_input(
            "1$2@3", "$,@"), [1, 2, 3])

    def test_parse_input_with_arbitrary_length_delimiter(self):
        self.assertEqual(StringCalculator().parse_input(
            "1$$$2$$$3"), [1, 2, 3])

    def test_extract_delimiter_without_delimiter(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "1,2,3"), ("1,2,3", ","))

    def test_extract_delimiter_with_comma_delimiter(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "//,\n1,2,3"), ("1,2,3", ","))

    def test_extract_delimiter_with_custom_delimiter(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "//$\n1,2,3"), ("1,2,3", "$"))

    def test_extract_delimiter_with_arbitrary_length_delimiter(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "//$$$\n1$$$2$$$3"), ("1$$$2$$$3", "$$$"))

    def test_extract_delimiter_with_multiple_delimiter(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "//$,@\n1$2@3"), ("1$2@3", "$,@"))

    def test_extract_delimiter_multiple_delimiters_arbitrary_length(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "//$$$,@@\n1$$$2@@3"), ("1$$$2@@3", "$$$,@@"))

    def test_extract_delimiter_multiple_delimiters_same_length(self):
        self.assertEqual(StringCalculator().extract_delimiter(
            "//$$,@@\n1$$2@@3"), ("1$$2@@3", "$$,@@"))

    def test_handle_negative_numbers_with_negative_inputs(self):
        self.assertRaises(Exception, StringCalculator(
        ).handle_negative_numbers, [1, -4, 5, -7])
