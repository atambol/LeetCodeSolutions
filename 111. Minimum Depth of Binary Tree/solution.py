# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if root.right and root.left:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
        elif root.right and not root.left:
            return 1 + self.minDepth(root.right)
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1
