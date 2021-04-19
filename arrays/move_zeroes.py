def move_zeroes(nums):
    '''
    # two pointers, left pointer finds zeroes
    # once a zero is found, we find the first non-zero and then swap these 2 pointers
    '''
    for left in range(len(nums)):
        if nums[left] == 0:
            right = left + 1
            while right < len(nums):
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    break
                right += 1
    return nums

def move_zeroes(nums):
    '''
    keep track of our first zero
    keep track of current number

    if current number is non-zero, swap with zero, increment the zero counter by 1 (will always find the left-most zero)

    '''
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
        print(nums)
    return nums


nums = [0,1,0,3,12]
res = move_zeroes(nums)
#print(f'\nres: {res}')
