import unittest

from hexagonal_tile_game import find_substring


class Test(unittest.TestCase):
    def test_simple(self):
        # 1, 2, 2 means node 1's 2nd out arrow goes to node 2
        tiles = [(1, 2, 2), (2, 3, 3), (3, 5, 4), (1, 3, 4), (4, 6, 1), (4, 1, 2), (2, 4, 4), (4, 2, 3), (2, 5, 1),
                 (3, 6, 2)]
        tile_chars = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        str_to_find = 'cab'
        actual = find_substring(tiles, tile_chars, str_to_find)
        expected = True
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)