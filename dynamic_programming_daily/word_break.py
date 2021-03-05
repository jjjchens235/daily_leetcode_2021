
def wordBreak(s, wordDict):
    # at each position see if it is a valid word
    # once a valid word is found, you need to check from the start of the next position


    # issue: if you use up a word, the remaining word must still be able to be filled up by some word in wordDic
    dp = [0] * len(s)
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] in wordDict:
                #for l in range(i, j):
                dp[i:j] = [1] * (j - i)
    return min(dp) != 0

# so everytime you find a word, you mark the whole word at 1, and you start from the next 0. You keep checking for a word and you mark it as one. As soon as you get to the end and you can't find a word

def wordBreak(s, wordDict):
    '''
    at each position, we compare our substring against the wordList.
    '''
    dp = [0] * len(s)
    found = -1
    for i in range(len(s)):
        if s[found+1: i+1] in wordDict:
        d


if __name__ == '__main__':
    s = 'catsandog'
    wordDict = ["cats","dog","sand","and","cat"]
    '''
    s = "applepenapple"
    wordDict = ["apple","pen"]
    s = "leetcode"
    wordDict = ["leet","code"]
    '''
    res = wordBreak(s, wordDict)
    print(f'\nres: {res}')

