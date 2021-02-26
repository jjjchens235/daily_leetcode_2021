def uniquePaths(m, n):
    '''
    logic: at every square, you want to add the value of the left, and of the top.
    You can't add the top if you're on the first row
    You can't add the left if you're on the first column.

    experience: initalizing this grid was the hardest part wasn't sure which loop should be the rows and which the cols. The answer is the most intuitive one though.
    Also, at first I tried initializing all values with -1, but it needs to be 0 since we are += it
    '''
    grid = [[0 for col in range(n)] for row in range(m)]
    print(grid)
    for row in range(m):
        for col in range(n):
            if row == col and row == 0:
                res = 1
            elif row == 0:
                res = grid[0][col - 1]
            elif col == 0:
                res = grid[row - 1][col]
            else:
                res = grid[row - 1][col] + grid[row][col - 1]
            grid[row][col] += res
    return grid[row][col]


def uniquePaths(m, n):
    '''
    # recursive solution
    logic:
    -Starting from the bottom right corner ( the end), check top square and left square, assuming those are valid squares
    - For each square, add the results of the two squares together

    experience:
    - This ended up being really frustrating.
    - I for some reason thought I had to add the current value of the square as well, but the value of the current square is not known yet
    '''
    memo = [[0 for col in range(n)] for row in range(m)]

    def _uniquePaths(row, col):
        if memo[row][col] != 0:
            return memo[row][col]
        if row == col and row == 0:
            return 1
        elif row == 0:
            res = _uniquePaths(0, col - 1)
        elif col == 0:
            res= _uniquePaths(row - 1, col)
        else:
            res= _uniquePaths(row - 1, col) + _uniquePaths(row, col - 1)
        memo[row][col] = res
        return res

    return _uniquePaths(m - 1, n - 1)


if __name__ == '__main__':
    res = uniquePaths(7, 3)
    print(f'\nres: {res}')
