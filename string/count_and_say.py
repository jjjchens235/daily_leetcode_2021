

def countAndSay(n):
    '''
    n_i = 1
    while n_i < n
    1) for each group of digits (identical digits)
        a. get the count
        b. get the digt itself
    store the current

    while i < len(digits):
        count_of_current = 1
        prev_str =
    '''
    def _countandSay(n, j, digits):

        count = 1
        res = ''
        for i in range(len(digits)):
            if (i != len(digits) - 1) and (digits[i] == digits[i + 1]):
                count += 1
            else:
                res += str(count) + digits[i]
                count = 1
        if j == n:
            return digits
        return _countandSay(n, j + 1, res)

    return _countandSay(n, 1, "1")
    #return countandSay(1)


def countAndSay(n):
    # for each current node check it's current count by comparing to previous
    # while i < n:
    # a) if curr == prev, increment count, else set count as 1
    def cas(digits):
        digits += '#'
        count = 1
        res = ''
        for i in range(len(digits) - 1):
            if digits[i] == digits[i + 1]:
                count += 1
            else:
                res += str(count) + digits[i]
                count = 1
        return res

    start = '1'
    for i in range(n - 1):
        start = cas(start)
    return start


if __name__ == '__main__':
    res = countAndSay(4)
    print(f'\nres: {res}')
