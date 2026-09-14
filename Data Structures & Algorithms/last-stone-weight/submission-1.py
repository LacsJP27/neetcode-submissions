class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = []
        heapq.heapify(maxHeap)
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        max1, max2 = 0, 0

        while len(maxHeap) > 1:
            max1 = -heapq.heappop(maxHeap)
            max2 = -heapq.heappop(maxHeap)

            res = abs(max1 - max2)

            if res != 0:
                heapq.heappush(maxHeap, -res)
        
        return -heapq.heappop(maxHeap) if len(maxHeap) > 0 else 0