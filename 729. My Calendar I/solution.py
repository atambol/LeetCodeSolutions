class MyCalendar(object):

    def __init__(self):
        # calendar with dummy slots for min and max
        self.calendar = [(-sys.maxsize-1, -sys.maxsize-1), (sys.maxsize, sys.maxsize)]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # maintain a sorted list and compare adjacent elements
        for i in range(len(self.calendar)-1):
            if self.calendar[i][1] <= start and self.calendar[i+1][0] >= end:
                # insert the new one in between
                self.calendar = self.calendar[:i+1] + [(start, end)] + self.calendar[i+1:]
                return True
        return False
                
            
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
