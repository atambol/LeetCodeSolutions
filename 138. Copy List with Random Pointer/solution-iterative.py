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
        
        # maintain two head pointers
        head1 = head
        head2 = RandomListNode(0)
        prev = head2
        
        # traverse nodes using the next pointer only and recreate the linked list
        while head:
            node = RandomListNode(head.label)
            self.visited[head] = node
            prev.next = node
            prev = node
            head = head.next
            
        # using the visited dictionary, update the random pointers in new list
        head = head1
        while head:
            if head.random:
                node = self.visited[head]
                node.random = self.visited[head.random]
            head = head.next
            
        return head2.next
