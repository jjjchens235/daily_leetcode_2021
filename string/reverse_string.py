def reverseString(s):
    return reversed(s)


def reverseString(s):
    # For odd length strings, once you get to the middle you can stop
    # For even strings, once you get to index == len(s) // 2, you can stop
    # corner cases, len(s) == 0 or len(s) == 1
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
    return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    res = reverseString(s)
    print(f'\nres: {res}')
