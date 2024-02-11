from case.caesar_cipher.caesar_cipher_utils import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher_non_alphabetic_input(self):
        self.assertEqual(caesarCipher('!@#$%^&*()', 4), '!@#$%^&*()')

    def test_caesar_cipher_empty_string(self):
        self.assertEqual(caesarCipher('', 2), '')

    def test_caesar_cipher_negative_shift(self):
        self.assertEqual(caesarCipher('thisisalongteststring', -7), 'mablbltehgzmxlmlmkbgz')

    def test_caesar_cipher_large_shift_value(self):
        self.assertEqual(caesarCipher('jumped', 26), 'jumped')

    def test_caesar_cipher_large_shift_value_wrap_around(self):
        self.assertEqual(caesarCipher('thequickbrownfox', 29), 'wkhtxlfneurzqira')

    def test_caesar_cipher_large_negative_shift_value(self):
        self.assertEqual(caesarCipher('abcdefg', -29), 'xyzabcd')

    def test_caesar_cipher_special_characters(self):
        self.assertEqual(caesarCipher('@#$%^&*()', 5), '@#$%^&*()')

    def test_caesar_cipher_long_string_shift_20(self):
        self.assertEqual(caesarCipher('ASongOfIceAndFire', 20), 'UMihaIzCwyUhxZcly')

    def test_caesar_cipher_long_string_wrap_around_shift_30(self):
        self.assertEqual(caesarCipher('interstellarvoyage', 30), 'mrxivwxippevzsceki')

    def test_caesar_cipher_long_string_wrap_around_shift_50(self):
        self.assertEqual(caesarCipher('ArtificialIntelligence', 50), 'YprgdgagyjGlrcjjgeclac')