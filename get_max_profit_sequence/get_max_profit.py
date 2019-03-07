'''
Return the index of buy and sell that would derive the maximum profit
'''
from typing import Tuple


def get_max_profit(list_of_stock_prices: list) -> Tuple[int, int, int]:
    '''
    Aim: Calculate the max profit from the given sequence of prices
    keep two pointers buy and sell. Initially set buy to first element and sell to second and
    store cur_pft as max_profit_seen so far. max_bi = 0, max_si = 1
    Maintain a rolling minimum of prices seen till one index back.
    max_pft_of_selling_now = current_price - rolling_minimum
    global_max_profit = max ( max_pft_of_selling_now, global_max_profit)
    '''
    current_buy_index = 0
    current_sell_index = 1
    current_profit = list_of_stock_prices[current_sell_index] - list_of_stock_prices[current_buy_index]
    # Set current best variables
    max_buy_index, max_sell_index, max_profit = current_buy_index, current_sell_index, current_profit
    for idx, t_price in enumerate(list_of_stock_prices[1:], start=1):
        if (t_price > list_of_stock_prices[current_sell_index]):
            # Same trade can be closed at a higher price by setting current_sell_index to idx
            current_sell_index = idx
            current_profit = list_of_stock_prices[current_sell_index] - list_of_stock_prices[current_buy_index]
        if ((t_price < list_of_stock_prices[current_buy_index]) and (idx + 1 < len(list_of_stock_prices))):
            # A new trade can be started with a lower buy price
            # And there is at least one element after this to close this trade.
            # However this means re-setting the current_sell_index too.
            current_buy_index = idx
            current_sell_index = idx + 1
            current_profit = list_of_stock_prices[current_sell_index] - list_of_stock_prices[current_buy_index]
        if (current_profit > max_profit):
            # Set current best variables
            max_buy_index, max_sell_index, max_profit = current_buy_index, current_sell_index, current_profit
    return (max_buy_index, max_sell_index, max_profit)


# Tests

import unittest


class Test(unittest.TestCase):
    def test_price_goes_up_then_down(self):
        _, _, actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_up_then_down_then_up(self):
        _, _, actual = get_max_profit([1, 5, 7, 3, 2, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        _, _, actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up_then_down(self):
        _, _, actual = get_max_profit([7, 2, 8, 9, 4, 3])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        _, _, actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        _, _, actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        _, _, actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)