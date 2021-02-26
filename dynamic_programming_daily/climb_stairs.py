
def climbStairs(n):
    '''
    recursion and memoization
    '''
    #n = 4
    # n = (0 or 1)
    #def _climbStairs(n):

    d = {}
    def _climbStairs(n):
        if n in (1, 2):
            return n
        if n-1 in d:
            res_one = d[n-1]
        else:
            res_one = _climbStairs(n-1)
            d[n-1] = res_one

        if n-2 in d:
            res_two = d[n-2]
        else:
            res_two = _climbStairs(n-2)
            d[n-2] = res_two
        return res_one + res_two
    return _climbStairs(n)


def climbStairs(n):
    '''
    bottom up
    '''
    l = [1, 2]
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
    return l[n-1]


if __name__ == '__main__':
    res = climbStairs(9)
    print(f'\nres: {res}')
