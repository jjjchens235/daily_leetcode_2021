def lengthOfLongestSubstring(s):
    '''
    keep track of the current window you're on using left and right pointer.
    keep track of how many characters are in the window so far, and the max window length

    if the right value has appeared in the set already, you need to move the left pointer to the index after that last occurence
    '''
    max_window = 0
    left = 0
    right = 0
    d = {}
    while right < len(s):
        if s[right] in d:
            max_window = max(max_window, right - left)
            left = max(left, d[s[right]] + 1)
        d[s[right]] = right
        right += 1
        print(left)
    return max(max_window, right - left)

s = "abcdefgahi"
res = lengthOfLongestSubstring(s)
print(f'\nres: {res}')
