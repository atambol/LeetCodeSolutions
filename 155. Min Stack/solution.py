class Node:
    def __init__(self, val, valMin):
        self.val = val
        self.min = valMin
        
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        valMin = min(self.stack[-1].min, x) if len(self.stack) > 0 else x
        node = Node(x, valMin)
        self.stack.append(node)
        # for i in range(len(self.stack)):
        #     print(self.stack[i].val, self.stack[i].min)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop() 
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1].val 

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1].min 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
