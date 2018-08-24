# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop

        heap = []
        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next

        head = ListNode(None)
        node = head
        while heap:
            node.next = ListNode(heappop(heap))
            node = node.next

        return head.next
