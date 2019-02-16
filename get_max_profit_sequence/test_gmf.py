from get_max_profit import get_max_profit


def __main__():
    stock_prices = [10, 7, 5, 4, 3, 2]  # 8, 11, 9]
    if (len(stock_prices) < 2):
        raise ValueError('stock_prices needs to be more than length 1')
    max_buy_index, max_sell_index = get_max_profit(stock_prices)
    max_profit = stock_prices[max_sell_index] - stock_prices[max_buy_index]
    if (max_sell_index <= max_buy_index):
        raise ValueError('You must hold for at least one time step after you buy')
    print('Max Profit = {} indices = {} and {}'.format(max_profit, max_buy_index, max_sell_index))


__main__()