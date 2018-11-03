# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return head
        
        curr = head
        prev = None

        # reach the point m
        i = 1
        while i != m:
            i += 1
            prev = curr
            curr = curr.next
        tail1 = prev
        tail2 = curr
        
        # reach the point n
        prev = None
        while i != n + 1:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            i += 1
            
        # join the three bits
        tail2.next = curr
        if m == 1:
            return prev
        else:
            tail1.next = prev
            return head
            
                
                
