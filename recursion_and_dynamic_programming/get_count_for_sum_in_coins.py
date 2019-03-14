'''Given an infinite supply of 25, 10, 5, 1 cent coins, calculate the number of ways to represent a sum of n cents'''

from typing import Dict, List, Tuple
import unittest

# Number of ways of making sum from list of allowed denominations. We are just recalling the max denomination here
map_sum_to_count: Dict[Tuple[int, int], int] = {}


def get_count_for_sum(req_sum: int, coin_denoms: List[int]) -> int:
    '''Dynamic programming'''
    if (not coin_denoms):
        if (req_sum > 0):
            return (0)
        else:
            return (1)
    # Assume coins sorted in descending order
    biggest_coin = coin_denoms[0]

    if (req_sum, biggest_coin) in map_sum_to_count:
        return (map_sum_to_count[(req_sum, biggest_coin)])
    else:
        retval: int = 0
        if req_sum <= 0:
            retval = 1
            map_sum_to_count[(req_sum, biggest_coin)] = retval
            return (retval)
        if (not coin_denoms) and (req_sum > 0):
            retval = 0
            map_sum_to_count[(req_sum, biggest_coin)] = retval
            return (retval)
        # If we are here, then (req_sum > 1)
        # Find the maximum number of this type of coin that can be in the sum
        max_c_num = (req_sum // biggest_coin)
        # Make a list of coin denominations not including this one
        # Note that lisr equality did not work
        # ref: https://stackoverflow.com/a/2612815/408936
        new_list_of_coins = coin_denoms[:]
        new_list_of_coins.remove(biggest_coin)
        for num_c in range(1 + max_c_num):
            # num_c is the number of coins of this type selected
            # Now onwards we are not allowing any more selection of this denomination
            retval = retval + get_count_for_sum(req_sum - (num_c * biggest_coin), new_list_of_coins)
        map_sum_to_count[(req_sum, biggest_coin)] = retval
        return (retval)


class Tests(unittest.TestCase):
    def test_1(self):
        req_sum: int = 6
        coin_denoms: List[int] = [25, 10, 5, 1]
        actual = get_count_for_sum(req_sum, coin_denoms)
        expected = 2
        self.assertEqual(actual, expected)

    def test_2(self):
        req_sum: int = 10
        coin_denoms: List[int] = [25, 10, 5, 1]
        actual = get_count_for_sum(req_sum, coin_denoms)
        expected = 4
        self.assertEqual(actual, expected)

    def test_3(self):
        req_sum: int = 15
        coin_denoms: List[int] = [25, 10, 5, 1]
        actual = get_count_for_sum(req_sum, coin_denoms)
        expected = 6
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)