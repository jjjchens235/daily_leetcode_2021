import heapq
class KthLargest:
    '''
    Experience:
    This problem was pretty hard to test
    Also I didn't have good intution for it.
    Also, I learned quite a bit about the heap, I never bothered to learn what a heap is as heapify abstracts away everything. In reality, a heap is a tree, where item in the list has children, that is the order is kept track of, and how we can return max or min at O(logn). Note that the heap.

    Logic:
    You want your priority queue to be at most k length. That way, you can just return the smallest number in the P queue.
    Inside init, you can pop until you reach k length.
    Inside add, you add numbers until you reach k.
    After that, you want to pop only if the number added is greater than the smaller number.

    Takeaways:
    The thing I would never have realized to keep the queue n length, I would have just kept appending to the queue, and keep calling nlargest, but nlargest is an inefficient function to use because it needs t * logn.



    '''

    def __init__(self, k, nums):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        while len(self.nums) > k:
            heapq.heappop(self.nums)


    def add(self, val):
        # if list doesn't have k nums yet
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)

        # list already contains k nums
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]


k = KthLargest(4, [10, 4, 5, 8, 2])
res = k.add(6)
print(f'\nres: {res}')
