# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # edge case
        if not intervals:
            return []
        
        # sort the intervals by start and end time
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        
        # merge into final solution
        sol = [intervals[0]]
        for i in intervals[1:]:
            if i.start <= sol[-1].end:
                # take the longer end
                sol[-1].end = max(sol[-1].end, i.end)
            else:
                sol.append(i)
                
        return sol
