# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = ListNode(None)
        node.next = head
        head = node
        
        # run the pointer for n times
        while n:
            node = node.next
            n -= 1
            
        # run another pointer behind it
        prev = head
        while node.next:
            prev = prev.next
            node = node.next
            
        # remove the node
        prev.next = prev.next.next
        return head.next
