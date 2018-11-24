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
        # edge case
        if not root:
            return 0
        
        # get depth of children and pass on the min depth
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if right and left:
            return 1 + min(right, left)
        elif not right:
            return 1 + left
        elif not left:
            return 1 + right
        else:
            return 1
        
