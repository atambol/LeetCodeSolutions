# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: (x.start, x.end))
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
            
        return True
