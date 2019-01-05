class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # dummy head
        node = ListNode(None)
        node.next = head
        head = node
        
        # count from 0
        m -= 1
        
        # iterate until m ceases
        prev = head
        node = head.next
        while m:
            n -= 1
            m -= 1
            prev = node
            node = node.next
        
        # reverse the nodes
        tail1 = prev
        prev.next = None
        prev = None
        tail2 = node
        while n:
            n -= 1
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            
        # tie up loose ends
        tail1.next = prev
        tail2.next = node
        
        return head.next
