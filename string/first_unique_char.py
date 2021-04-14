def first_unique_char(s):
    # two for loops? The first is a dictionary where v is incremented for each occurence of a character
    # the second for loop checks the value of the counter
    from collections import Counter
    d = Counter(s)
    for i, char in enumerate(s):
        if d[char] == 1:
            return i
    return -1


if __name__ == '__main__':
    s = 'loveleetcode'
    res = first_unique_char(s)
    print(f'\nres: {res}')
