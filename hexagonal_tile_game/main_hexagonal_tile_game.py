import unittest


class Test(unittest.TestCase):
    def test_simple(self):
        # 1, 2, 2 means node 1's 2nd out arrow goes to node 2
        tiles = [(1, 2, 2), (2, 3, 3), (3, 5, 4), (1, 3, 4), (4, 6, 1), (4, 1, 2), (2, 4, 4), (4, 2, 3), (2, 5, 1),
                 (3, 6, 2)]
        tile_chars = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        actual = get_num_seating_arrangements(N, 3, [seating])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)