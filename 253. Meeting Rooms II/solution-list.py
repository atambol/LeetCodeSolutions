# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) < 2:
            return len(intervals)
        
        start = []
        end = []
        
        # sort the intervals
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
            
        start.sort()
        end.sort()
        
        n = len(end)
        i = 1
        count = 0
        j = 0
        
        # traverse each interval and update count
        while i < n:
            count = max(count, abs(i-j))
            while end[j] <= start[i]:
                j += 1
            i += 1
            
        return max(count, abs(i-j))
