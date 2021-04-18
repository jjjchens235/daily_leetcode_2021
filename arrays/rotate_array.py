

def rotate_array(nums, k):
    # rotate k % len(nums) times
    # each rotation is like this:
    # a) tmp = (nums[-1])
    # b) del(nums[-1])
    # c) [tmp]  + nums

    for i in range(k):
        prev = nums[-1]
        for j in range(len(nums)):
            temp = nums[j]
            nums[j] = prev
            prev = temp
    print(nums)


def rotate_array(nums, k):
    new_nums = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        new_i = (i+k) % len(nums)
        print(f'\nnew_i: {new_i}')
        new_nums[new_i] = nums[i]
    nums[:] = new_nums
    print(nums)



nums = [1,2,3,4,5,6,7]
k = 3
rotate_array(nums, k)
