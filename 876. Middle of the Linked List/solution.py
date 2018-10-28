# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fptr = head
        sptr = head
        while fptr and fptr.next:
            sptr = sptr.next
            fptr = fptr.next.next
            
        return sptr
