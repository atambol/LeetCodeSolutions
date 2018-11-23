# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # check for edge cases
        if not head:
            return
        
        # reverse the list
        head = self.reverseList(head)
        
        # increment by one and update the nodes
        carry = True
        node = head
        prev = None
        while carry and node:
            node.val += 1
            if node.val == 10:
                node.val = 0
            else:
                carry = False
            prev = node
            node = node.next
        
        # check if there is a carry left after all nodes are incremented
        if carry:
            node = ListNode(1)
            prev.next = node
            prev = prev.next
            
        # reverse the list back
        return self.reverseList(head)
    
    def reverseList(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
