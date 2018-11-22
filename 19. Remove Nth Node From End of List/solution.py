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
        # edge cases
        if not head:
            return head
        
        # insert a false head at the front to remove edge cases due to removal of first node
        node = ListNode(None)
        node.next = head
        head = node
        
        # move fptr for n + 1 iterations
        i = 0
        fptr = head
        while i <= n:
            i += 1
            fptr = fptr.next
            
        # move sptr until fptr reaches the end
        sptr = head
        while fptr:
            fptr = fptr.next
            sptr = sptr.next
        
        # remove the node
        sptr.next = sptr.next.next
        return head.next
        
