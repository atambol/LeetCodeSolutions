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
        k, node = self.mykthSmallest(root, k)
        return node.val
        
    def mykthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int, int
        """
        # edge case
        if not root:
            return k, None
        
        # look left
        k, node = self.mykthSmallest(root.left, k)
        if node:
            return k, node
        
        # look at root
        k -= 1
        
        if not k:
            return k, root
        
        # look right
        return self.mykthSmallest(root.right, k)
