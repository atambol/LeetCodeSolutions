# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        else:
            size = 0
            node = head
            while node:
                node = node.next 
                size += 1
            
            if size == k or size == 0 or size == 1:
                return head
            
            if size < k:
                k = k%size

            if k == 0:
                return head
            
            newhead = None
            node = head
            if size - k > 0:
                for x in range(size-k-1):
                    node = node.next

                prev = node
                node = node.next
                newhead = node
                prev.next = None
                while node.next != None:
                    node = node.next
                node.next = head
            return newhead
