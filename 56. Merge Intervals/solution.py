# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # edge case
        if not intervals:
            return intervals
        
        # sort by start time
        intervals.sort(key=lambda x: x.start)
        
        # merge overlaps
        sol = [intervals[0]]
        for i in intervals[1:]:
            if i.start <= sol[-1].end:
                sol[-1].end = max(i.end, sol[-1].end)
            else:
                sol.append(i)
                
        return sol
