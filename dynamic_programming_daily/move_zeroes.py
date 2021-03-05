
def moveZeroes(nums):
    #goal is to move left and right pointer
    # left pointer is on the first zero, right pointer is on the first non zero
    #left = 0
    for left in range(0, len(nums)):
        right = left + 1
        if nums[left] == 0:
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums) and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
        #print(nums)
    return nums


if __name__ == '__main__':
    nums = [4,2,4,0,0,3,0,5,1,0]
    res = moveZeroes(nums)
    print(f'\nres: {res}')
