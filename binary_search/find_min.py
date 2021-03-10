
def findMin(nums):
    # return the minimum element in the array

    # similiar to regular binary search
    #if mid > right, then we scan nums[mid+1: right]
    #else we scan left to mid -1

    start = 0
    end = len(nums) - 1
    while end > start:
        print(nums[start: end+1])
        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    return nums[end]

if __name__ == '__main__':
    nums = [3,4,5,1,2]
    nums = [4,5,6,7,0,1,2]
    nums = [11,13,15,17]
    res = findMin(nums)
    print(f'\nres: {res}')
