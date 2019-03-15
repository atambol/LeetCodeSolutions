"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # edge case
        if not head:
            return head
        
        # create and save nodes
        clone = {}
        h = Node(None, None, None)
        old = head
        new = h
        while old:
            new.next = Node(old.val, None, None)
            new = new.next
            clone[old] = new
            old = old.next
            
        # attach nodes
        old = head
        new = h.next
        while old:
            if old.next:
                new.next = clone[old.next]
            if old.random:
                new.random = clone[old.random]
            old = old.next
            new = new.next
            
        return h.next
