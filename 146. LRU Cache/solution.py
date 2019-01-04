class Node:
    def __init__(self, k, v):
        self.val = v
        self.key = k
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.map = {}
        self.cap = capacity
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        
        # take the node out
        node.next.prev = node.prev
        node.prev.next = node.next
        
        # push it to the top
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev = node
        node.prev.next = node
        
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if the node exists in the list
        if key in self.map:
            node = self.map[key]
            node.val = value
            
            # take the node out
            node.next.prev = node.prev
            node.prev.next = node.next

            # push it to the top
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            node.prev.next = node
        
        # a new node should be created
        else:
            if not self.cap:
                # take the least recently used node out of list
                node = self.tail.next
                self.tail.next = node.next
                node.next.prev = self.tail
                
                # remove the node from map
                self.map.pop(node.key)
                
            else:
                self.cap -= 1
            
            # create a new node
            node = Node(key, value)
            
            # push it to the top
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            node.prev.next = node
                      
            # add it to the map
            self.map[key] = node
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
