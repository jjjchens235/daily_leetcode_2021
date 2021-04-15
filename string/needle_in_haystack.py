
def str_str(haystack, needle):
    #compare needle == haystack[0 + len(needle) -1]
    # two pointer problem, where start and end make up the length of needle. We go through every substring of haystack that equals the length of needle and compare to needle.
    if needle == '':
        return 0
    start = 0
    end = len(needle) - 1
    while end < len(haystack):
        if needle == haystack[start: end + 1]:
            return start
        start += 1
        end += 1
    return -1


if __name__ == '__main__':
    haystack = 'hello'
    needle = 'lll'
    res = str_str(haystack, '')
    print(f'\nres: {res}')
