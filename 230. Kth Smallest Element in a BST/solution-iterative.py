# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # perform inorder traversal
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                # decrement the count
                k -= 1
                
                # the kth node is found when k = 0
                if not k:
                    return node.val
                
                # keep searching
                node = node.right
