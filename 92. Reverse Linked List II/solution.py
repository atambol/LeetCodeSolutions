class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # attach a dummy head
        node = ListNode(None)
        node.next = head
        head = node
        node = head.next
        prev = head
        
        # find the mth node
        l = 0
        while m > 1:
            prev = node
            node = node.next
            m -= 1
            n -= 1
            
        # break the list here
        tail1 = prev
        head2 = node
        
        # reverse the next n - m nodes
        prev = None
        while n >= 1:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            n -= 1
            
        # join the lists
        tail1.next = prev
        head2.next = node
        
        return head.next
