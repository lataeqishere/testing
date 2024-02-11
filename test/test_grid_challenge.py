from case.grid_challenge.grid_challenge_utils import gridChallenge
import unittest

class Grid_Challenge_Test(unittest.TestCase):
    def test_grid_challenge_yes(self):
        grid = [
            'efghi',
            'lmnop',
            'qrstu',
            'abcde'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')

    def test_grid_challenge_no(self):
        grid = [
            'ebc',
            'gaf',
            'dhf'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')

    def test_grid_challenge_single_row(self):
        grid = ['abcd']
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_grid_challenge_special_characters(self):
        grid = [
            '@#$', '%^&',
            '*()!', '!@#'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')

    def test_grid_challenge_mixed_characters_yes(self):
        grid = [
            'kmbaz',
            'olnbc',
            'pocad',
            'qredf'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')

    def test_grid_challenge_mixed_characters_no(self):
        grid = [
            'kmbaz',
            'olnbc',
            'pocad',
            'qrexf'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')

    def test_grid_challenge_long_strings(self):
        grid = [
            'yrtopqklmn',
            'xdcvgfklop',
            'asekmbujhq'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')