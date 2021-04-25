def set_zeroes(matrix):
    '''
    2 * (m * n) time complexity
    m * n space complexity
    Each time we find a zero,
    '''
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix


def set_zeroes(matrix):
    '''
    how to get constant space complexity
    not allowed to store any elements, so if we get to a zero, that means that the zeroes for all corresponding rows/cols need to be converted
    was thinking of each zero, converting all the corresponding 1's to zeroes as well, but this doesn't work because you will create zeroes in the future that will create even more zeroes
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                # for all rows and cols, in i and j, we nee to conver them to 'x'
                for row in range(len(matrix)):
                    if matrix[row][j] != 0:
                        matrix[row][j] = 'x'
                for col in range(len(matrix[i])):
                    if matrix[i][col] != 0:
                        matrix[i][col] = 'x'
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'x':
                matrix[i][j] = 0

    return matrix



matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
res = set_zeroes(matrix)
print(f'\nres: {res}')
