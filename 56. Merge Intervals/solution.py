# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # edge case
        if not intervals:
            return intervals
        
        # sort the intervals by start position
        intervals.sort(key=lambda x: (x.start, x.end))
        
        merged = [intervals[0]]
        for i in intervals[1:]:
            if i.start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, i.end)
                
            else:
                merged.append(i)
                
        return merged
