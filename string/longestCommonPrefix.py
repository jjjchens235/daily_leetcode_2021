def longestCommonPrefix(strs):
    #for each char of each str
    # check if it matches the current char


    # for the first element in the list, map it to a dictionary, where k: v is index, letter
    # For each character, increment min_count

    # Now for each string, check if it matches the dictionary values, if it stops matching, break and update min_count
    if not strs:
        return ''
    d = {i: char for i, char in enumerate(strs[0])}
    min_count = len(d)
    for i in range(1, len(strs)):
        count = 0
        for char_i in range(len(strs[i])):
            try:
                if d[char_i] == strs[i][char_i]:
                    count += 1
                # current word stopped matching
                else:
                    break
            # current word is longer than original word
            except KeyError:
                break
        min_count = min(count, min_count)
    return strs[0][: min_count]


def longestCommonPrefix(strs):
    # get the shortest string in strs
    # compare shortest against every subsequent string by character and check if the characters match,
    # if it stops matching, update shortest to where it stopped matching
    if not strs:
        return ''
    shortest = min(strs, key=len)
    for i in range(len(strs)):
        for j in range(len(shortest)):
            if shortest[j] != strs[i][j]:
                shortest = shortest[:j]
                break
    return shortest



if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    res = longestCommonPrefix(strs)
    print(f'\nres: {res}')
