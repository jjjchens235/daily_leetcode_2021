
def productExceptSelf(nums):
    '''
    incorrect
    '''
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


def productExceptSelf(nums):
    '''
    let's start all over- it's a new day
    Here are the following conditions
    1) If there's no zeroes in the array at all, we can divide the total product / current num
    2) If there's 1 zero, all the numbers except the zero position are taken up
    3) If there's two zeroes, all numbers are zeroes
    '''
    res = []
    total = 1
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total *= num

    for num in nums:
        if zero_count > 1:
            res.append(0)
        elif zero_count == 0:
            res.append(total // num)
        elif zero_count == 1:
            if num == 0:
                res.append(total)
            else:
                res.append(0)
    return res



if __name__ == '__main__':
    nums = [-1,1,0,-3,3]
    res = productExceptSelf(nums)
    print(f'\nres: {res}')
