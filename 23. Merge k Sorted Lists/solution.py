# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # create a heap of size k - number of lists
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
            
        # extract and pushback
        head = ListNode(None)
        node = head
        while heap:
            _, l = heapq.heappop(heap)
            node.next = l
            node = node.next
            l = l.next
            node.next = None
            if l:
                heapq.heappush(heap, (l.val, l))
                
        return head.next
