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
        if not intervals:
            return 0
        
        heap = []
        intervals.sort(key=lambda x: x.start)
        
        rooms = 0
        for i in intervals:
            while heap and heap[0] <= i.start:
                heapq.heappop(heap)
                
            heapq.heappush(heap, i.end)
            rooms = max(rooms, len(heap))
            
        return rooms
