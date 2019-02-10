# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        group = set(G)
        count = 0
        node = head
        while node:
            i = node.val
            if node.val in group:
                if not node.next or node.next.val not in group:
                    count += 1
            node = node.next
        return count
