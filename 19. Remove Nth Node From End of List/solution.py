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
        # attach a dummy head
        node = ListNode(None)
        node.next= head
        head = node
        
        # run a pointer for n iterations
        fptr = head.next
        while n > 0:
            fptr = fptr.next
            n -= 1
        
        # run another pointer to reach the node to be delete
        sptr = head
        while fptr:
            sptr = sptr.next
            fptr = fptr.next
        
        # delete
        sptr.next = sptr.next.next
        
        return head.next
        
