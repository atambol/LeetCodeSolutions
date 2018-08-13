class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

        
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.len = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        
        
    def display(self):
        node = self.head
        while (node != self.tail):
            print(node.val)
            node = node.next
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # self.display()
        try:
            node = self.map[key]
            node.prev.next, node.next.prev = node.next, node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next.prev = node
            return node.val
        except KeyError:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # self.display()
        try:
            node = self.map[key]
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next.prev = node
        except KeyError:
            if self.len < self.capacity:
                self.len += 1
            else:
                node = self.tail.prev
                self.tail.prev = node.prev
                node.prev.next = self.tail
                del self.map[node.key]

            node = Node(key, value)
            node.prev = self.head
            node.next = self.head.next
            self.head.next = node
            node.next.prev = node
            self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
