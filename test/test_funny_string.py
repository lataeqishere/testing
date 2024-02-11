from case.funny_string.funny_string_utils import funnyString
import unittest


class Funny_String_Test(unittest.TestCase):
    def test_funny_string_funny_case(self):
        self.assertEqual(funnyString('hello'), 'Not Funny')

    def test_funny_string_not_funny_case(self):
        self.assertEqual(funnyString('world'), 'Not Funny')

    def test_funny_string_empty_string(self):
        self.assertEqual(funnyString(''), 'Funny')

    def test_funny_string_single_character(self):
        self.assertEqual(funnyString('x'), 'Funny')

    def test_funny_string_repeated_characters(self):
        self.assertEqual(funnyString('aaaaaa'), 'Funny')

    def test_funny_string_all_characters_same_distance(self):
        self.assertEqual(funnyString('xyvw'), 'Funny')

    def test_funny_string_large_distance_between_characters(self):
        self.assertEqual(funnyString('xyzp'), 'Not Funny')

    def test_funny_string_large_distance_between_characters_not_funny(self):
        self.assertEqual(funnyString('xyzzp'), 'Not Funny')

    def test_funny_string_special_characters(self):
        self.assertEqual(funnyString('@#$%'), 'Not Funny')

    def test_funny_string_mixed_characters(self):
        self.assertEqual(funnyString('lmnop'), 'Funny')