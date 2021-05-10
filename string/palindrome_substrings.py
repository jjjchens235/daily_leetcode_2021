def countSubstrings(s):
    def check(l, r):
        res = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            else:
                break
        return res

    count = 0
    for i in range(len(s)):
        even = check(i-1, i)
        odd = check(i, i)
        count = even + odd + count
    return count


if __name__ == '__main__':
    s = "aba"
    res = countSubstrings(s)
    print(f'\nres: {res}')
