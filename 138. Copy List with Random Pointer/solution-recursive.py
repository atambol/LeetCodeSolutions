# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    # visited dictionary from old node to new node
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        # if head is visited already, return the node created for it
        if head in self.visited:
            return self.visited[head]
        else:
            # create a new node and push it to visited nodes
            node = RandomListNode(head.label)
            self.visited[head] = node
            
            # connect its next and random pointer
            node.next = self.copyRandomList(head.next)
            node.random = self.copyRandomList(head.random)
            
            return node
            
