import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, MaxHeapItem(nums[i]))
        i = 0
        res = None
        for i in range(k - 1):
            heapq.heappop(heap).val
        res = heapq.heappop(heap).val
        return res

        
class MaxHeapItem:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        return self.val > other.val