

def minimumTotal(triangle):
    '''
    logic:
    - from each position, you check the previous two options, left_up, and right_up.
    The previous two options should also be running totals that you're overwrriting at each position.

    -caveats, if you're at the right most row, you won't be able to check right_up.
    If you're at the left most row, you won't be able to check left_up
    '''
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            left_up = float('inf')
            right_up = float('inf')
            if i != 0:
                if j != 0:
                    left_up = triangle[i-1][j-1]
                if j != len(triangle[i]) - 1:
                    right_up = triangle[i-1][j]
                triangle[i][j] += min(left_up, right_up)
            #print(triangle)
    return min(triangle[-1])

if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = minimumTotal(triangle)
    print(f'\nres: {res}')
