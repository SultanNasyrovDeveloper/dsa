"""
Given an array representing prices of some product day by day.
Every day manufacture creates only 1 product. Calculate max profit we can get
by selling at days. We can sell or not to sell at any day.
"""
Price = int


def calculate_max_profit(prices: list[Price]) -> Price:
    result = 0
    last_sell_price = prices[-1]
    last_sell_amount = 1
    current_index = len(prices) - 2
    while current_index >= 0:
        current_price = prices[current_index]
        if current_price > last_sell_price:
            result += last_sell_price * last_sell_amount
            last_sell_price = current_price
            last_sell_amount = 1
        else:
            last_sell_amount += 1
        current_index -= 1
    result += last_sell_price * last_sell_amount
    return result


assert calculate_max_profit([1, 1, 1]) == 3
assert calculate_max_profit([1, 1, 3, 1, 2, 1]) == 14
assert calculate_max_profit([1, 2, 1, 1, 3, 1, 1, 2, 1]) == 22
