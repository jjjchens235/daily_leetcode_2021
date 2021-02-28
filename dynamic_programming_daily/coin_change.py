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
        #return min(_coinChange(coins, remaining - 1, turn), _coinChange(coins, remaining - 2, turn), _coinChange(coins, remaining - 5, turn))
    return _coinChange(coins, amount, 0)


#what am i doing wrong? Solution needs to check every sinle coin combination
# each time you pass in a new list that includes the difference
def coinChange(coins, amount):
    # at each position
    #This intition is more wrong then the above recursive one btw
    if amount == 0:
        return  0
    nums = [amount for i in range(len(coins))]
    steps = 0
    while max(nums) > 0:
        steps += 1
        for i in range(len(coins)):
            nums[i] -= coins[i]
            if nums[i] == 0:
                return steps
        print(nums)
    return -1

def coinChange(coins, amount):
    # I cheated an am looking at the solutin now, don't want to spend too much time on one problem
    dp = [0] + [float('inf') for i in range(amount)]
    print(dp)
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
            print(dp)

def coinChange(coins, amount):
    # recursive solution: at each position, you need to try all the coins and subtract it from the balance
    # not complete yet, I'm not sure how to generalize this based on the number of available coins
    def _coinChange(coins, remaining, turns):
        if remaining == 0:
            return 0
        elif remaining < 0:
            return -1
        min_ = float('inf')
        #turn += 1
        #for coin in coins:
        for coin in coins:
            res = _coinChange(coins, remaining - coin, turns)
            if res >= 0 and res < min_:
                min_ = 1 + res
        if min_ == float('inf'):
            turns[remaining - 1] = -1
        else:
            turns[remaining - 1] = min_
        return turns[remaining - 1]
    return _coinChange(coins, amount, [None] * amount)

def coinChange(coins, amount):
    # Shing explained the problem to me
    # Create a list the size of amount, called dp

    # Each value of dp represents the minimum amount of coins to get to that index value. So let's take a dp = [0, 1, 1, 2]. To get to a value of 1, it takes 1 coin, to get to the value of 2, it takes 1 coins and to get to a value of 3, it takes 2 coins. Sidenote: this implies we have access to at least the coins [1, 2]
    #  at each index of dp, we want to assign it the minimum amount of coins it takes to get sum up to that index
    #To calc the min amount, we do index - coin,
    #if there's no remainder, it means it takes 1 coin to create that index value.
    #and if there's a remainder, we check if that remainder exists in a previous value of the array.

    #so take coins=[2,3], and amount= 5
    #dp = [0, -1, -1, -1, -1, -1] (we added a 0 at the front to make it easier to index)
    # at index 1, we ask ourselves if we can create that coin, no we can't get to a value of 1, with coins of 2 and 3
    # at index=2, we ask ourselves if we can create a coin with value of 2. The answer is yes it takes us 1 coin, so dp = [0, -1, 1, -1, -1, -1]
    # at index 3, same quesiton, this time we can create that index using coin 3, so dp = [0, -1, 1, 1, -1, -1].
    # at index 5, we ask ourselves if we can create a coin of value 5, using one of our coins. So, we try coin 2, and we get a remainder this time of 3. So, we check index=3, to see what the value is. This previous index value represents the number of coins it takes to create a value of 3. At the index of 3, dp[3] = 1, so, d[[5] = 1 + 1


    if amount == 0:
        return 0
    dp = [-1] * (amount + 1)
    dp[0] = 0

    for i in range(1, len(dp)):
        min_ = float('inf')
        for coin in coins:
            remainder = i - coin
            if remainder == 0:
                dp[i] = 1
            elif remainder > 0:
                if dp[remainder] != -1 and dp[remainder] < min_:
                    dp[i] = 1 + dp[remainder]
                    min_ = dp[remainder]

            #dp[i] = 1
    return dp[-1]


if __name__ == '__main__':
    res = coinChange([1,2,5], 11)
    print(f'\nres: {res}')
