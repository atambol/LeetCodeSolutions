class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.map = {}

    def get(self, key: int) -> int:
        head = self.head
        tail = self.tail
        
        if key in self.map:
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = head.prev
            head.prev = node
            node.prev.next = node
            node.next = head
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        head = self.head
        tail = self.tail

        node = None    
        if key in self.map:
            node = self.map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        
        if not node:
            if not self.cap:
                node = tail.next
                self.map.pop(node.key)
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                self.cap -= 1
            node = Node(key, value)
            self.map[key] = node
        
        node.prev = head.prev
        head.prev = node
        node.prev.next = node
        node.next = head

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
