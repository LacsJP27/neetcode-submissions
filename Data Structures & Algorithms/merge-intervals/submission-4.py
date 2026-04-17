class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        # sort by the start value
        # use lambda function to designate key
        intervals.sort(key = lambda x: x[0])
        # overlaps if the nextStart < prevEnd
        # if they overlap then take prevStart and max of end and prevEnd
        # prevEnd: 3, 5
        # prevStart: 1
        res = [intervals[0]]


        for start, end in intervals:
            prevEnd = res[-1][1]
            if start <= prevEnd:
                res[-1][1] = max(end, prevEnd)
            else:
                res.append([start, end])

        return res