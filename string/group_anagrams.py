def group_anagrams(strs):
    d = {}
    res = []
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in d:
            d[sorted_s].append(s)
        else:
            d[sorted_s] = [s]
    for anagrams in d.values():
        res.append(anagrams)
    return res

strs = ["eat","tea","tan","ate","nat","bat"]
res = group_anagrams(strs)
print(f'\nres: {res}')
