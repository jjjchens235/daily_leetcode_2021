
def maxProfit(prices):
    '''
    if the stock to the left of you is smaller, you always buy it. Now, if the stock to the right of you is bigger, you don't sell yet.
    '''
    profit = 0
    i = 1
    while i < len(prices):
        if prices[i] > prices[i-1]:
            buy_price = prices[i-1]
            while i+1 < len(prices) and prices[i+1] > prices[i]:
                i += 1
            profit += prices[i] - buy_price
            i += 1
        i += 1
    return profit


if __name__ == '__main__':
    prices = [2, 5, 100, 200]
    prices = [7,1,5,3,6,4]
    prices = [1,2,3,4,5]
    prices = [7,6,4,3,1]
    res = maxProfit(prices)
    print(f'\nres: {res}')
