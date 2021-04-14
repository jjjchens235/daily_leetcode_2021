def reverse(x):
    #start, keep track if is_negative
    # main logic: to get the last digit of a number mod by 10
    # add that digit to a string
    # Then remove that digit by // 10
    # end: check if is_negative, if true, add a negative sign to the string

    res = '0'
    is_negative = False
    if x < 0:
        is_negative = True
        x = x * -1
    while x != 0:
        res += str(x % 10)
        x //= 10
    res = int(res)
    if is_negative:
        res *= -1
    if res > 2**32-1 or res < -2**32:
        return 0
    return res


if __name__ == '__main__':
    x = 10000
    res = reverse(x)
    print(f'\nres: {res}')
