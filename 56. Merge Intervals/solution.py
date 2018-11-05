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
        # Sort by second key and then first key
        intervals.sort(key=lambda interval: interval.start)

        # Check and merge
        sol = []
        for interval in intervals:
            if sol:
                if sol[-1].end >= interval.start:
                    sol[-1].end = max(sol[-1].end, interval.end)
                else:
                    sol.append(interval)
            else:
                sol.append(interval)
                
        return sol
