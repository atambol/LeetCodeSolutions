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
        fptr = head
        sptr = head
        
        # find cycle
        cycle = False
        while fptr and fptr.next:
            fptr = fptr.next.next
            sptr = sptr.next
            
            if fptr == sptr:
                cycle = True
                break
                
        if not cycle:
            return None
        
        # find the beginning of cycle
        fptr = head
        while sptr != fptr:
            fptr = fptr.next
            sptr = sptr.next
            
        return sptr
        
