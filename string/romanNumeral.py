def intToRoman(num):
    # algorithim: iterate through ordered dict {int: symbol}, and for each int, largest to smallest, do a num % int. If the num is returned, that means that int is bigger than num. If
    # If num is smaller than int, than we need to figure out how many of those ints are in num, i.e how many 100's are in 298.
    # nums now equals the remainder, i.e 98
    from collections import OrderedDict
    d = OrderedDict()
    d[1000] = 'M'
    d[900] = 'CM'
    d[500] = 'D'
    d[400] = 'CD'
    d[100] = 'C'
    d[90] = 'XC'
    d[50] = 'L'
    d[40] = 'XL'
    d[10] = 'X'
    d[9] = 'IX'
    d[5] = 'V'
    d[4] = 'IV'
    d[1] = 'I'

    s = ''
    for k in d.keys():
        rem = num % k
        if rem != num:
            times = num // k
            s += (d[k] * times)
            num = rem
    return s


if __name__ == '__main__':
    num = 298
    res = intToRoman(num)
    print(f'\nres: {res}')
