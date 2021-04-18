

def max_profit(prices):
    # buy if price < next_price
    # sell if price > next_price
    prices.append(0)
    profit, i = 0, 0
    while i < len(prices) - 1:
        if prices[i] < prices[i + 1]:
            buy_price = prices[i]
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
            profit += (prices[i] - buy_price)
        i += 1
    return profit


prices = [1,2,3,4,5]
res = max_profit(prices)
print(f'\nres: {res}')
