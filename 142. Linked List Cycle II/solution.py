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
        # edge cases
        if not head:
            return None
        
        # fast pointer and slow pointer technique to find cycle
        fptr = head
        sptr = head
        prev = None
        cycle = False
        while fptr and fptr.next and not cycle:
            prev = sptr
            fptr = fptr.next.next
            sptr = sptr.next
            if sptr == fptr:
                cycle = True
                
        if not cycle:
            return None
        else:
            # the meeting point of two pointers in not the answer
            # cycle can begin anywhere in the list
            # to find that, increment both pointers with same pace now
            sptr = head
            while sptr != fptr:
                fptr = fptr.next
                sptr = sptr.next
                
            return sptr
