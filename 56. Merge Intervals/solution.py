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
        if len(intervals) < 2:
            return intervals
        res = []
        intervals.sort(key=lambda interval: interval.start)
        j = 0
        res.append(intervals[j])
        for i in range(1, len(intervals)):
            if res[j].end >= intervals[i].start:
                res[j].end = max(intervals[i].end, res[j].end)
            else:
                res.append(intervals[i])
                j += 1
            i += 1
        # self.display(intervals)
        return res
        
    def display(self, intervals):
        for i in intervals:
            print(i.start, i.end)
