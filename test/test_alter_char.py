from case.alter_char.alternating_char_utils import alternatingCharacters
import unittest

class Alternating_Characters_Test(unittest.TestCase):
    def test_given_AABABABBA(self):
        s = "AABABABBA"
        result = alternatingCharacters(s)
        self.assertEqual(result,2)

    def test_given_AAAABAABBB(self):
        s = "AAAABAABBB"
        result = alternatingCharacters(s)
        self.assertEqual(result,6)

    def test_given_AAAA(self):
        s = "AAAA"
        result = alternatingCharacters(s)
        self.assertEqual(result,3)

    def test_given_BLANK(self):
        s = ""
        result = alternatingCharacters(s)
        self.assertEqual(result,0)

    def test_given_(self):
        s = "ISUGHPISUEBGSKDJBNGSDGJKNJJSDGSG"
        result = alternatingCharacters(s)
        self.assertEqual(result,1)

    def test_given_PPOTAEYAKKINKAWWAHEEHEE(self):
        s = "PPOTAEYAKKINKAWWAHEEHEE"
        result = alternatingCharacters(s)
        self.assertEqual(result,5)

    def test_given_EIEIZA(self):
        s = "EIEIZA"
        result = alternatingCharacters(s)
        self.assertEqual(result,0)

    def test_given_HEEHEE(self):
        s = "HEEHEE"
        result = alternatingCharacters(s)
        self.assertEqual(result,2)

    def test_given_A1000(self):
        s = "A" * 1000
        result = alternatingCharacters(s)
        self.assertEqual(result,999)

    def test_given_AB50(self):
        s = "AB" * 50
        result = alternatingCharacters(s)
        self.assertEqual(result,0)