from case.two_char.two_char_utils import alternate
import unittest

class Two_characters_Test(unittest.TestCase):
    def test_alternate_example_1(self):
        self.assertEqual(alternate('beabeefeab'), 5)

    def test_alternate_example_2(self):
        self.assertEqual(alternate('abcdefgxyz'), 2)

    def test_alternate_empty_string(self):
        self.assertEqual(alternate(''), 0)

    def test_alternate_single_character(self):
        self.assertEqual(alternate('x'), 0)

    def test_alternate_repeated_characters(self):
        self.assertEqual(alternate('aaaa'), 0)

    def test_alternate_special_characters(self):
        self.assertEqual(alternate('@#$%^&*'), 2)

    def test_alternate_mixed_characters(self):
        self.assertEqual(alternate('abccddee'), 2)

    def test_alternate_long_string(self):
        self.assertEqual(alternate('abcbabcbabcbabcbabcbabcbabcb'), 14)

    def test_alternate_long_string_2(self):
        self.assertEqual(alternate('zxyxzyxzyxzyxzyxzyxzyxzyxzyxzyx'), 21)