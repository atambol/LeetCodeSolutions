# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # edge condition
        if not head or not head.next:
            return None
        
        # detect cycle
        fptr = head
        sptr = head
        cycle = False
        while fptr and fptr.next and not cycle:
            fptr = fptr.next.next
            sptr = sptr.next
            cycle = fptr == sptr
            
        if not cycle:
            return None
        
        # detect start
        fptr = head
        while fptr != sptr:
            fptr = fptr.next
            sptr = sptr.next
            
        return sptr
        
            
        
