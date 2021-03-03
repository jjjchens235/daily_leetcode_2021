def maxSubArray(nums):
    # at each point, add to itself or start all over if it's a negative numbe
    nums.insert(0, 0)
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums[1:])

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    #nums = [-1]
    res = maxSubArray(nums)
    print(f'\nres: {res}')
