class MyCalendarTwo(object):

    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # check for overlap
        for s, e in self.overlaps:
            if end > s and e > start:   # condition of overlap
                return False
            
        # find new overlaps
        for s, e in self.events:
            if end > s and e > start:
                self.overlaps.append((max(start, s), min(end, e)))
        
        # add events
        self.events.append((start, end))
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
