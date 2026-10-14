class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # non-overlapping intervals
        # intervals[i] = [start_i, end_i]
        # start and end time at ith interval
        # sorted in ascending order by start_i

        # newInterval = [start, end]
        # insert so still sorted
        # and still no overlapping intervals
        # may merge overlapping intervals
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x : x[0])

        return self.merge(intervals)

    def merge(self, intervals):
        #[1, 4], [2, 7], [5, 8]
        # [1, 7], [5, 8]
        res = [intervals[0]]

        # i = 3
        for start, end in intervals[1:]:
            prevEnd = res[-1][1]
            if prevEnd >= start:
                # merge them here
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])

        return res


