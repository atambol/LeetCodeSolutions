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
        if not intervals:
            return intervals
        
        intervals.sort(key=lambda i: (i.start, i.end))
        sol = [intervals[0]]
        
        for i in intervals[1:]:
            if sol[-1].end >= i.start:
                sol[-1].end = max(sol[-1].end, i.end)
            else:
                sol.append(i)
        return sol
