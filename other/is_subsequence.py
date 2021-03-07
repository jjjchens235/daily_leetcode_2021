def isSubsequence(s, t):
    # check if
    i = 0
    if i == len(s):
        return True
    for target in t:
        if s[i] == target:
            i += 1
        if i == len(s):
            return True
    return False


if __name__ == '__main__':
    s = 'axc'
    t = 'ahbgdc'
    res = isSubsequence(s, t)
    print(f'\nres: {res}')
