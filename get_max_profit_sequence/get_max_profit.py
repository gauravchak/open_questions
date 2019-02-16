'''
Return the index of buy and sell that would derive the maximum profit
'''
from typing import Tuple


def get_max_profit(list_of_stock_prices: list) -> Tuple[int, int]:
    '''
    Return the index of buy and sell that would derive the maximum profit
    '''
    current_buy_index = 0
    current_sell_index = 1
    current_profit = list_of_stock_prices[current_sell_index] - list_of_stock_prices[current_buy_index]
    max_buy_index = 0
    max_sell_index = 1
    max_profit = current_profit
    for idx in range(1, len(list_of_stock_prices)):
        if (list_of_stock_prices[idx] > list_of_stock_prices[current_sell_index]):
            # Same trade can be closed at a higher price
            current_sell_index = idx
            current_profit = list_of_stock_prices[current_sell_index] - list_of_stock_prices[current_buy_index]
        if ((list_of_stock_prices[idx] < list_of_stock_prices[current_buy_index])
                and (idx + 1 < len(list_of_stock_prices))):
            # A new trade can be started with a lower buy price
            # And there is at least one element after this to close this trade.
            # However this means re-setting the current_sell_index too.
            current_buy_index = idx
            current_sell_index = idx + 1
            current_profit = list_of_stock_prices[current_sell_index] - list_of_stock_prices[current_buy_index]
        if (current_profit > max_profit):
            max_buy_index = current_buy_index
            max_sell_index = current_sell_index
            max_profit = current_profit
    return (max_buy_index, max_sell_index)
