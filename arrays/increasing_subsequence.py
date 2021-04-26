def increasing_triplet(nums):
    '''
    4/25/2021

    need to keep track of
    a) minimum number
    b) second min number

    if current number > second min num, return true
    '''
    min_num, second_min = float('inf'), float('inf')
    for num in nums:
        if num > second_min:
            return True
        elif num < min_num:
            min_num = num
        # second_min check
        elif num > min_num and num < second_min:
            second_min = num
    return False

nums = [8, 9, 3, 5]
res = increasing_triplet(nums)
print(f'\nres: {res}')
