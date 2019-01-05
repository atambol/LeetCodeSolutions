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
        max_count = 0
        count = 0
        ends = []
        
        # sort the intervals
        intervals.sort(key=lambda i: (i.start, i.end))
        
        # traverse each interval and update count
        for i in intervals:
            # pop expired intervals
            while ends and ends[0] <= i.start:
                heapq.heappop(ends)
                count -= 1
                
            # insert the new interval
            count += 1
            heapq.heappush(ends, i.end)
            
            # calculate maxcount
            max_count = max(max_count, count)
            
        return max_count
            
