import heapq
class KthLargest:

    def __init__(self, k, nums):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        while len(self.nums) > k:
            heapq.heappop(self.nums)


    def add(self, val):
        heapq.heappushpop(self.nums, val)
        #heapq.heappop(self.nums)
        return self.nums[0]


k = KthLargest(4, [10, 4, 5, 8, 2])
res = k.add(6)
print(f'\nres: {res}')
