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
        # dummy head
        ptr = ListNode(None)
        ptr.next = head
        head = ptr
        prev = head
        ptr = head.next
        
        # create difference of n
        while n:
            n -= 1
            ptr = ptr.next
            
        # run two pointers
        while ptr:
            ptr = ptr.next
            prev = prev.next
            
        prev.next = prev.next.next
        return head.next
