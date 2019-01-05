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
            return []
        
        # sort the intervals by start time
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        
        # create the new merged list
        sol = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= sol[-1].end:
                sol[-1].end = max(sol[-1].end, interval.end)
            else:
                sol.append(interval)
                
        return sol
        
