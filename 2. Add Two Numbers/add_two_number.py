# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        prev = None
        carry = 0
        while l1 or l2 or carry == 1:
            newnode = ListNode(0)
            if l1:
                newnode.val += l1.val
                l1 = l1.next
            if l2:
                newnode.val += l2.val
                l2 = l2.next
            newnode.val += carry
            carry = 0
            if newnode.val >= 10:
                carry = 1
                newnode.val %= 10
                
            
            if head:
                prev.next = newnode

            else:
                head = newnode
            prev = newnode

        return head
            
            
