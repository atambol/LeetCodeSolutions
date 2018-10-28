# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Handle edge cases
        if not head or not head.next:
            return head
        
        # General flow
        ptr = ListNode(None)
        ptr.next = head
        head = ptr
        ptr = ptr.next 
        prev = head
        
        while ptr and ptr.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            tmp.next = prev.next
            prev.next = tmp
            
            prev = ptr
            ptr = ptr.next

        return head.next
