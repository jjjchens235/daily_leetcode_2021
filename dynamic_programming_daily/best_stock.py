def maxProfit(prices):
    # at each position, you want to compare to the minimum of all previous positions. That would be your profit at that position
    min_price = float('inf')
    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        prices[i] = price - min_price
    #print(prices)
    return max(prices)

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    res = maxProfit(prices)
    print(f'\nres: {res}')
