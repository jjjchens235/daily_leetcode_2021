

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


matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = rotate(matrix)
print(f'\nres: {res}')
