def single_number(nums):
    '''
    Create a dict with k, v of num: count
    '''
    from collections import Counter
    c = Counter(nums)
    for num in nums:
        if c[num] == 1:
            return num
