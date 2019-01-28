# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        heap = []
        stack = []
        while stack or root:
            if root:
                heapq.heappush(heap, (abs(root.val-target), root.val))
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
                
        kSmallest = heapq.nsmallest(k, heap)
        return [x[1] for x in kSmallest]
