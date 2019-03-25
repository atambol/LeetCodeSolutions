class MyCalendarThree:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> int:
        self.intervals.append((start, end))
        self.intervals.sort(key=lambda x: x[0])
        
        # count overlaps
        heap = []
        count = 0
        for i in range(len(self.intervals)):
            while heap and self.intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
                
            heapq.heappush(heap, self.intervals[i][1])
            count = max(count, len(heap))
        return count
            
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
