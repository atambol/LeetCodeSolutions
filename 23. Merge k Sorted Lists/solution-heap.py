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
        # assume there are m list with n nodes each on average
        # create a min heap for each node's value, O(mn*log(mn))
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        # pop elements from heap and add it to a linked list
        # total elements = mn, heappop = log(mn), Complexity = O(mn*log(mn))
        head = ListNode(None)
        node = head
        while heap:
            node.next = ListNode(heapq.heappop(heap))
            node = node.next
        
        return head.next
