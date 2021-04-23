def is_valid_suduoku(board):
    '''
    3 conditons

    1. Check all items in list are not the same
    2. Check All the items in each list with the same index
    3. Check all items between board[i] : board[i+2], and board[i][j] : board[i][j+2]

    Create 3 list of 9 sets, each list representing each condition
    The key is the index of the list, and it represents the row/col/grid we are currently on, and the set represents all the values within that row/col/grid

    To do #3, must check which grid using an if condition based on x and y
    '''

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    grid = [set() for _ in range(9)]

    for x in range(9):
        for y in range(9):
            current = board[x][y]

            # check if duplicate in row
            if current != '.' and current in rows[x]:
                return False
            else:
                rows[x].add(current)

            # check if duplicate in col
            if current != '.' and current in cols[y]:
                return False
            else:
                cols[y].add(current)

            # check if in grid
            if x < 3 and y < 3:
                grid_index = 0
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 3 and y < 6:
                grid_index = 1
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 3 and y < 9:
                grid_index = 2
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 6 and y < 3:
                grid_index = 3
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 6 and y < 6:
                grid_index = 4
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 6 and y < 9:
                grid_index = 5
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 9 and y < 3:
                grid_index = 6
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 9 and y < 6:
                grid_index = 7
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
            if x < 9 and y < 9:
                grid_index = 8
                if current != '.' and current in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(current)
    return True

board = \
    [["8","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]
res = is_valid_suduoku(board)
print(f'\nres: {res}')
