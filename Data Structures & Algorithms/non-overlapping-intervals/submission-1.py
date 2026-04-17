class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        # get the first end val
        prevEnd = intervals[0][1]

        # start at the second interval
        # comparing the previous end (1st end to start)
        # with the next start(the second interval at the start of loop)
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # the new prevEnd is now the current
                # you're comparing this new prevEnd to the next start
                prevEnd = end
            else:
                res += 1
                # how to "remove the interval"
                # just have to update the prevEnd to the end that ends first
                # use the minimu end because you want minimum removals
                # smaller end means more likely to not overlap then large end of intervals
                prevEnd = min(end, prevEnd)
        
        return res


                