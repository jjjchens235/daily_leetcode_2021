
def minPathSum(grid):
    '''
    recursive solution

    1) logic:
    - need to keep track of the max value at every possible combination and compare it to what would happen if you took the other option.
    - if you do this recursively, you should start tracking at grid[-1][-1] the last square, and go towards the top left square.
    - The possible combinations, starting at the BOTTOM right are either going up, or going left. Note that you can't go up if you're on the first row. You can't go left if you're on the first column.
    - Rows are based off of the first index, and columns are based on the second index. I find this unintuitive, one way to figure this out is to figure out how going from grid[0] to grid[1] works, you are moving down row-wise. When you go from grid[0][0] -> grid[0][1], you are moving to the right col-wise.

    2) experience: Pretty pleased with myself, got the logic down on the first submission, though it times out.

    3) takeaways:
        - Start at the end with recursive solutions, same as house robbers.
        - I have a hard time with matrix problems, especially the indexes

'''
    def _minPathSum(grid, row_index, col_index):
        if row_index == col_index and col_index == 0:
            return grid[0][0]
        if row_index == 0:
            return grid[0][col_index] + _minPathSum(grid, row_index, col_index -1)
        if col_index == 0:
            return grid[row_index][0] + _minPathSum(grid, row_index-1, col_index)
        return min(grid[row_index][col_index] + _minPathSum(grid, row_index, col_index-1), grid[row_index][col_index] + _minPathSum(grid, row_index-1, col_index))
    return _minPathSum(grid, len(grid)-1, len(grid[0])-1)

def minPathSum(grid):
    '''
    bottom up

    1) logic: Actually quite simple,
    -loop through every square.
    - At each square, you want to overwrite it's current value with current_value + min(leftSquare, topSquare).
    - can't compare against leftsquare and topsquare if it leads to index error
    2) experience: This one took me a long time even though I already had recurisve solution figured out. I was convinced we had to check the next squares at each position rather than the two previous squares.
    '''
    len_row = len(grid)
    len_col = len(grid[0])
    for row in range(0, len_row):
        for col in range(0, len_col):
            if row == 0 and col == 0:
                prev = 0
            #can't go up
            elif row == 0:
                prev = grid[row][col-1]
            #can't go left
            elif col == 0:
                prev = grid[row-1][col]
            else:
                prev = min(grid[row-1][col], grid[row][col-1])
            grid[row][col] += prev
    return grid[row][col]


if __name__ == '__main__':
    #grid = [[1,2,3],[4,5,6]]
    grid = [[1,2],[1,1]]
    res = minPathSum(grid)
    print(f'\nres: {res}')
