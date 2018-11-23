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
        # edge cases
        if not head:
            return 
        
        # create a dummy head for ease of modification
        node = ListNode(None)
        node.next = head
        head = node
        
        # get the length of the list and batch count
        l = 0
        node = head.next
        while node:
            l += 1
            node = node.next
        batchCount = l//k
        
        # reverse nodes in batches of k
        # maintain tail of prev batch and tail after the current batch is reversed to connect batched together
        node = head.next
        prev = None
        tailOfPrevK = head
        batchesDone = 0
        # this prevents reversal of last batch that neednt be reversed
        while batchesDone < batchCount:
            i = 0
            tailAfterReverse = node
            # batch size is k
            while i < k:
                i += 1
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
                
            # reconnect the newly reversed batch with previous batch
            # prepare for next reversal
            tailOfPrevK.next = prev
            tailOfPrevK = tailAfterReverse
            prev = tailAfterReverse
            prev.next = node
            batchesDone += 1
            
        return head.next
                
        
        
