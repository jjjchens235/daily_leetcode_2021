
def productExceptSelf(nums):
    zero_count = 0
    total = 1
    for num in nums:
        if num == 0:
            zero_count += 1
            if zero_count == 2:
                total = 0
                break
        else:
            total *= num
    res = []
    for num in nums:
        if num == 0:
            res.append(total)
        else:
            res.append(total // num)
    return res


if __name__ == '__main__':
    nums = [1,2,3,4]
    res = productExceptSelf(nums)
    print(f'\nres: {res}')
