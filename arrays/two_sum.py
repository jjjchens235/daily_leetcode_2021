def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        diff = (target - num)
        if diff in d:
            return [d[diff], i]
        d[num] = i

nums = [2,7,11,15]
target = 9
res = two_sum(nums, target)
print(f'\nres: {res}')
