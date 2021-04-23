
def threeSum(nums):
    '''
    first thought is to iterate through the entire list and create a dictionary
    Then you go through the nums again, using two pointers for every possible combination, check to see if their possible combination exists

    # edge case is if diff = a = b, this is not allowed
    # other edge case is if the difference exists in the dictionary but it's already being used in either a or b
    '''

    # shoot this solution contains duplicate triplets :(((
    # didn't read the instructions closely enough clearly
    res = []
    from collections import Counter
    c = Counter(nums)
    for i in range(len(nums)):
        j = 1
        while i + j < len(nums):
            print(f'\ni: {i}, {j}')
            diff = - (nums[i] + nums[i + j] )
            if diff in c:
                # can't have duplicate values
                if diff == nums[i] and diff == nums[i + j]:
                    j += 1
                    continue
                elif (diff == nums[i]) or (diff == nums[i + j]):
                    if c[diff] > 1:
                        res.append([nums[i], nums[i + j], diff])
                else:
                    res.append([nums[i], nums[i + j], diff])

            j += 1
    return res

nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print(f'\nres: {res}')

