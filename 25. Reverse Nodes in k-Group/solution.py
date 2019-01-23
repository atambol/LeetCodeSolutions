# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # insert dummy node
        node = ListNode(None)
        node.next = head
        head = node
        node = head.next
        
        # count the number nodes
        count = 0
        while node:
            node = node.next
            count += 1
            
        # count the iterations
        n = count // k
        
        # reverse the nodes in groups of k
        node = head.next
        prev = head
        while n:
            tail1 = prev
            tail2 = node
            prev = None
            for i in range(k):
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
                
            tail1.next = prev
            prev = tail2
            n -= 1
        prev.next = node
        return head.next
            
