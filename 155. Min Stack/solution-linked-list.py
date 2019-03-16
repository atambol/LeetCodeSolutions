class Node:
    def __init__(self, x, y):
        self.num = x
        self.min = y
        self.next = None
        self.prev = None
        
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = Node(None, None)
        self.tail = self.head

    def push(self, x: int) -> None:
        # get the minimum number
        minNum = self.tail.min if self.tail != self.head else x
        minNum = min(minNum, x)
        node = Node(x, minNum)
        
        # insert new node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        

    def pop(self) -> None:
        if self.tail == self.head:
            return
        
        self.tail = self.tail.prev

    def top(self) -> int:
        return self.tail.num

    def getMin(self) -> int:
        return self.tail.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
