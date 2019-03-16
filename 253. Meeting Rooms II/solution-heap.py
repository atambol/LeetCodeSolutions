# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        # sort the intervals list
        intervals.sort(key = lambda x: (x.start, x.end))
        
        # push the end times into the heap 
        count = 0
        for i in intervals:
            while heap and heap[0] <= i.start:
                heapq.heappop(heap)
        
            heapq.heappush(heap, i.end)
            count = max(count, len(heap))
            
        return count
        
