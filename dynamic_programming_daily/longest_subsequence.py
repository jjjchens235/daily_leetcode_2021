def lengthOfLIS(nums):
    #non working solution, passes all provided test ccases but fails when going up, down, up
    nums.insert(0, float('-inf'))
    cp = nums.copy()
    max_count = 0
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            max_count += 1
        '''
        else:
            count = 1
        '''
        #max_count = max(max_count, count)
        cp[i] = max_count
    print(cp)
    return cp[-1]

def lengthOfLIS(nums):
    # n^2 solution, dp
    # at each position, get it's longest subarray streak up to that point and if bigger, plus 1, else nothing.
    # this video was really good: https://www.youtube.com/watch?v=CE2b_-XfVDk&ab_channel=TusharRoy-CodingMadeSimple
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i+1):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)



if __name__ == '__main__':
    #nums = [10,9,2,5,3,7,101,18]
    #nums = [0,1,0,3,2,3]
    #nums = [7,7,7,7,7,7,7]
    #nums = [50, 55, 60, 40, 49, 41, 42]
    nums = [3, 4, -1, 0, 6, 2, 3]
    res = lengthOfLIS(nums)
    print(f'\nres: {res}')
