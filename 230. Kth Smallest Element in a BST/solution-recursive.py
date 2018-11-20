# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Beats 99%
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        val, found = self.mykthSmallest(root, k, 0)
        return val
        
    def mykthSmallest(self, root, k, n):
        # Null node condition
        if not root:
            return n, False
        
        # check the left subtree
        n, found = self.mykthSmallest(root.left, k, n)
        if found:
            return n, found
        else:
            # check self
            if n + 1 == k:
                return root.val, True
            else:
                # check the right subtree
                return self.mykthSmallest(root.right, k, n+1)
        
