def removeDuplicates(nums):
    # compare current against previous
    # if current is not equal to previous increment count, make sure to update previous
    if not nums:
        return 0
    prev = nums[0]
    i = 1
    while i < len(nums):
        # if duplicate, delete
        if nums[i] == prev:
            del(nums[i])
        else:
            prev = nums[i]
            i += 1
    return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    res = removeDuplicates(nums)
    print(f'\nres: {res}')
