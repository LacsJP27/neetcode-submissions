"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x : x.start)

        if len(intervals) <= 1:
            return True

        i = 1
        while i < len(intervals):
            nxtStrt, end = intervals[i].start, intervals[i - 1].end

            if nxtStrt < end:
                return False

            i += 1

        return True
            

            

