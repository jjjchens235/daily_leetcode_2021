
def characterReplacement(s, k):
    '''
    at each position, you want to see if you have can create a longest substring with that particular word, go left and right
    If you encounter a different char

    '''
    #TODO wrong answer
    def replace_char(s, start_index, k):
        l = 0
        start_char = s[start_index]
        while start_index >= 0 and k >= 0:
            if s[start_index] == start_char:
                l += 1
            else:
                if k > 0:
                    l += 1
                k -= 1
            start_index -= 1
        return l

    l = 0
    max_len = float('-inf')
    for i in range(len(s)):
        l = replace_char(s, i, k)
        max_len = max(l, max_len)
    return max_len

s = "ABADCB"
k = 2

res = characterReplacement(s, k)
print(f'\nres: {res}')
