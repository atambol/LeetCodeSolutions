# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # edge cases
        if not head:
            return head
        if not head.next:
            return head
        
        # get length
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        
        # bring k between 0 to n-1
        k = k%n
        if k == 0:
            return head
        
        # k nodes counted from start
        k = n - k - 1
        node = head
        while k:
            node = node.next
            k -= 1
            
        # break the list
        tail1 = node
        head2 = node.next
        node = node.next
        tail1.next = None

        # find the tail of the last node
        while node.next:
            node = node.next
            
        # join the lists
        node.next = head
        return head2
