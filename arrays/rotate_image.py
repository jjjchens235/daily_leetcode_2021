

def rotate(matrix):
    '''
    allocating another 2D array (against the instructions)

    '''
    res = []
    for j in range(len(matrix[0])):
        inner = []
        for i in reversed(range(len(matrix))):
            inner.append(matrix[i][j])
        res.append(inner)
    return res

def rotate(matrix):
    """
    math theory, two stepsL
    1) reverse row-wise
    2) make the first column become the first row, for all columns
    1 2 3
    4 5 6
    """
    # first step
    for i in range(len(matrix) // 2):
        matrix[i], matrix[len(matrix) - i - 1] = matrix[len(matrix) - i - 1], matrix[i]
    # second step
    # need to make sure that any swapped value is not swapped again
    for i in range(len(matrix)):
        j = 0
        #for j in range(len(matrix)):
        while i + j < len(matrix):
            matrix[i][i + j], matrix[i+j][i] = matrix[i+j][i], matrix[i][i+j]
            j += 1
    return matrix

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
res = rotate(matrix)
print(f'\nres: {res}')
