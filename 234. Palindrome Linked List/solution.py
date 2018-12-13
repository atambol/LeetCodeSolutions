# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # edge cases
        if not head:
            return True
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
    
        # O(n) time and O(n) space solution
        # find the middle point of the list
        sptr = head
        fptr = head
        while fptr and fptr.next:
            sptr = sptr.next
            fptr = fptr.next.next

        # important condition to manage both even and odd sized linked lists
        newhead = sptr
        if fptr:
            newhead = newhead.next
        
        # reverse the list after mid point
        prev = None
        while newhead:
            tmp = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = tmp
            
        # compare the two heads
        newhead = prev
        while head and newhead:
            if head.val != newhead.val:
                return False
            head = head.next
            newhead = newhead.next
            
        return True
