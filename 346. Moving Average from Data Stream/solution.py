from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.dq = deque()
        self.size = size
        self.sum = 0
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.dq) == self.size:
            left = self.dq.popleft()
            self.sum -= left
        self.sum += val
        self.dq.append(val)
        return self.sum/len(self.dq)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
