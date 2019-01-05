# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # dummy head
        node = ListNode(None)
        node.next = head
        head = node
        
        # get length of list
        n = 0
        node = head.next
        while node:
            node = node.next
            n += 1
            
        # reverse nodes in iterations
        i = n//k
        tail1 = head
        node = head.next
        tail2 = node
        while i:
            prev = None
            
            # reverse
            for j in range(k):
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
                            
            # tie up the ends
            tail1.next = prev
            tail1 = tail2
            tail2 = node
            i -= 1
        
        # final loose end
        tail1.next = node
        
        return head.next
