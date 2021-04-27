'''
This question is concerned about bit manipulation
This is a really good refresher though she goes a bit too fast:
https://www.youtube.com/watch?v=NLKQEOgBAnw&ab_channel=HackerRank
'''

def hammingWeight(n):
    '''
    4/26/2021: naive solution
    convert n to a string, count the number of 1's it has
    '''
    s = str(n)
    res = 0
    for char in s:
        if char == '1':
            res += 1
    return res

def hammingWeight(n):
    '''
    4/26/2021, actual bit solution, still naive
    take input and apply a & mask whose digit is 1 at the end, each loop shift the mask's 1 digit to the left so that eventually you check every input place
    '''
    count = 0
    mask = 1

    for i in range(32):
        if (n & mask) > 0:
            count += 1
        mask <<= 1
    return count


n = 11111111111111111111111111111101
res = hammingWeight(n)
print(f'\nres: {res}')
