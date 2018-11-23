# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # edge cases
        if not head:
            return head
        
        # make dummy head
        node = ListNode(None)
        node.next = head
        head = node
        node = node.next
        prev = head
        
        # remove nodes with val 
        while node:
            if node.val == val:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
                
        return head.next
        
