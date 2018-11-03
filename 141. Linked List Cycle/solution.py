# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return False
        
        sptr = head
        fptr = head.next
        
        while sptr and fptr and fptr.next:
            if sptr == fptr:
                return True
            
            sptr = sptr.next
            fptr = fptr.next.next
            
        return False
