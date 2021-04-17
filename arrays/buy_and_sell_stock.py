def maxProfit(prices):
    # keep track of  min_price
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        max_profit = max(price - min_price, max_profit)
        min_price = min(min_price, price)
    return max_profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    res = maxProfit(prices)
    print(f'\nres: {res}')
