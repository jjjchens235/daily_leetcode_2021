def coinChange(coins, amount):
    # recursive solution: at each position, you need to try all the coins and subtract it from the balance
    # not complete yet, I'm not sure how to generalize this based on the number of available coins
    def _coinChange(coins, remaining, turn):
        if remaining == 0:
            return turn
        elif remaining < 0:
            return float('inf')
        turn += 1
        #for coin in coins:
        return min(_coinChange(coins, remaining - 1, turn), _coinChange(coins, remaining - 2, turn), _coinChange(coins, remaining - 5, turn))
    return _coinChange(coins, amount, 0)


if __name__ == '__main__':
    res = coinChange([1,2,5], 11)
    print(f'\nres: {res}')
