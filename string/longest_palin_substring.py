def longestPalindrome(s):
    '''
    4/25/2021
    The bruteforce solution is to go through every substring and check if it's palindromic

    My initial gut instinct tells me that the ideal solution involves some sort of sliding window
    Would need to involve every single possible starting and ending combination, if those match, you just move inwards

    We loop through the string, treating each index as the pivot point.
    For each pivot point/center, it could either be two letters or one letter, we must test both
    For each pivot point, we want to see the max substring palindrome by moving outwards
    '''
    def palindrome_at(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[(left + 1): (right - 1) + 1]

    max_str = ''
    for i in range(len(s)):
        max_str = max(max_str, palindrome_at(s, i, i), palindrome_at(s, i, i + 1), key=len)
    return max_str


s = 'dcaac'
res = longestPalindrome(s)
print(f'\nres: {res}')
