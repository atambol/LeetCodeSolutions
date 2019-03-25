class MyCalendarThree:

    def __init__(self):
        self.intervals = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.intervals[start] += 1
        self.intervals[end] -= 1
        
        keys = list(self.intervals)
        keys.sort()
        
        # running sum technique
        count = 0
        rsum = 0
        for k in keys:
            rsum += self.intervals[k]
            count = max(count, rsum)
        
        return count
        # complexity
        # n = number of intervals
        # O(nlogn)
            
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
