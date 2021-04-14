

def is_anagram(s, t):
    from collections import Counter
    s = Counter(s)
    t = Counter(t)
    return s == t


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    res = is_anagram(s, t)
    print(f'\nres: {res}')
