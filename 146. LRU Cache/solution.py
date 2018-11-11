class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    # remove least recently used node
    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = None
        self.prev = None
    
    # insert a new node
    def insert(self, nxt, prev):
        self.next = nxt
        nxt.prev = self
        self.prev = prev
        prev.next = self
    
    # update the node to most recent node
    def update(self, head):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = head
        self.prev = head.prev
        head.prev = self
        self.prev.next = self
        
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        
        self.KeyNotFound = -1
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head
        self.records = {}
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.records:
            node = self.records[key]
            # update the node as most recently used
            node.update(self.head)
            return node.value
        else:
            return self.KeyNotFound

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # check if the key already exists
        if key in self.records:
            node = self.records[key]
            node.value = value
            node.update(self.head)
            
        else:
            # if the capacity of the cache is reached
            if len(self.records) == self.capacity:
                # remove the least recently used node
                node = self.tail.next
                self.records.pop(node.key, None)
                node.remove()

            # Create a new node
            node = Node(key, value)
            self.records[key] = node

            # insert the new node next to head
            node.insert(self.head, self.head.prev)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
