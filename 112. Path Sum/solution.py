# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        else:
            if not root.left and not root.right and root.val == sum:
                return True
            else:
                val = sum - root.val
                return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)
        
