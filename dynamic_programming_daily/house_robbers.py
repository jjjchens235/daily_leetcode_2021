

# House Robbers
def rob(nums):
    def _rob(nums, i):
        if i < 0:
            return 0
        return max(nums[i] + _rob(nums, i - 2), _rob(nums, i - 1))
    # let's see, n, or (n - 1 + n+1)
    return _rob(nums, len(nums) - 1)


def rob(nums):
    '''
    memoization (store)
    test using this test case [10, 8, 6, 4, 2, 5]
    '''
    d = {}
    def _rob(nums, i):
        if i < 0:
            return 0
        if i in d:
            res = d[i]
        else:
            res = max(nums[i] + _rob(nums, i - 2), _rob(nums, i - 1))
            d[i] = res
        return res
    # let's see, n, or (n - 1 + n+1)
    return _rob(nums, len(nums) - 1)




def rob(nums):

    #bottom up

    #[ 10, 8, 4, 2, 5]

    # num[i] + max_sum or nums[i-1]

    #for every new index, keep track of what the max sum is at that index

    if len(nums) <= 2:
        return max(nums)

    new_nums = [nums[0], nums[1]]
    for i in range(2, len(nums)):
        max_sum = max(nums[i] + new_nums[i-2], new_nums[i-1])
        new_nums.append(max_sum)
        print(new_nums)

    return new_nums[-1]


if __name__ == '__main__':
    nums = [10, 8, 6, 4, 2, 5]
    res = rob(nums)
    print(f'\nres: {res}')
