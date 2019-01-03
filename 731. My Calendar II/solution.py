class MyCalendarTwo:

    def __init__(self):
        # save events
        self.events = []
        
        # save previous overlaps
        self.doubles = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # check if this event overlaps with any of the previous overlaps (triple booking)
        for s, e in self.doubles:
             if s < end and start < e:
                    return False
        
        # add new overlaps
        for s, e in self.events:
            if s < end and start < e:
                self.doubles.append((max(s, start), min(e, end)))
                
        # store this event
        self.events.append((start, end))
        return True
    
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
