import unittest
from get_num_seating_arrangements import get_num_seating_arrangements


class Test(unittest.TestCase):
    def test_one_row(self):
        N: int = 1
        seating: str = 'EET|EEET|EEE'
        actual = get_num_seating_arrangements(N, 3, [seating])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
