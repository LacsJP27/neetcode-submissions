"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # [[start_1,end_1],[start_2,end_2],...] (start_i < end_i)
        (0,30), (5,10), (15,2)
        intervals = sorted(intervals, key=lambda x : x.start)
        min_heap = []

        for inter in intervals:
            if min_heap and min_heap[0] <= inter.start:
                    heapq.heappop(min_heap)
            heapq.heappush(min_heap, inter.end)
        
        # rooms [40, 20, 25]

        return len(min_heap)
