
def threeSum(nums):
    '''
    first thought is to iterate through the entire list and create a dictionary
    Then you go through the nums again, using two pointers for every possible combination, check to see if their possible combination exists

    # edge case is if diff = a = b, this is not allowed
    # other edge case is if the difference exists in the dictionary but it's already being used in either a or b
    '''

    # shoot this solution contains duplicate triplets :(((
    # didn't read the instructions closely enough clearly
    #TODO
    '''
    Not sure exactly how to fix duplicate issue
    In the end I looked at the solution, and it was a little complicated to invest time into, will come back to this if I have time
    '''
    res = []
    from collections import Counter
    c = Counter(nums)
    for i in range(len(nums)):
        j = 1
        while i + j < len(nums):
            print(f'\ni: {i}, {j}')
            diff = - (nums[i] + nums[i + j] )
            if diff in c:
                if diff == nums[i] and diff == nums[i + j]:
                    if c[diff] > 2:
                        res.append([nums[i], nums[i + j], diff])
                elif (diff == nums[i]) or (diff == nums[i + j]):
                    if c[diff] > 1:
                        res.append([nums[i], nums[i + j], diff])
                else:
                    res.append([nums[i], nums[i + j], diff])

            j += 1
    return res

def threeSum(nums):
    '''
    # https://fizzbuzzed.com/top-interview-questions-1/#:~:text=A%20basic%2C%20O(n3,just%20use%20three%20for%20loops.
     - sort nums
     - 3 pointer solution
        - i  is current number
        - left, always right of current  by 1
        - right, always starts at the end
    - If nums[i] + nums[j] + nums[k] > 0, k --
    - else if < 0, then j++
    '''

    res = []
    nums = sorted(nums)
    i = 0
    while i < len(nums):
        # iterate current until it's a different number
        while i != 0 and i < len(nums) and nums[i] == nums[i-1]:
            i += 1
        left = i + 1
        right = len(nums) - 1
        while left < right:
            # if sum == 0
            if nums[i] + nums[left] + nums[right] == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # corner case, need to make sure we don't repeat the same combo more than once, keep iterating either left or right, but not both - we chose left
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            # sum > 0, need to make right smaller
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            # sum < 0, need to make left bigger
            else:
                left += 1
        i += 1
    return res





nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print(f'\nres: {res}')

