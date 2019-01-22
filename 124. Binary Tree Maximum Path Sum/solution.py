# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum, maxPath = self.mymaxPathSum(root)
        return maxSum
    
    def mymaxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # not child
        if not root.left and not root.right:
            return root.val, root.val
        # only right child
        elif not root.left and root.right:
            rSum, rPath = self.mymaxPathSum(root.right)
            maxPath = max(rPath+root.val, root.val)
            maxSum = max(rSum, maxPath)
            return maxSum, maxPath
        # only left child
        elif not root.right and root.left:
            lSum, lPath = self.mymaxPathSum(root.left)
            maxPath = max(lPath+root.val, root.val)
            maxSum = max(lSum, maxPath)
            return maxSum, maxPath
        # both child
        else:
            rSum, rPath = self.mymaxPathSum(root.right)
            lSum, lPath = self.mymaxPathSum(root.left)
            maxPath = max(lPath+root.val, rPath+root.val, root.val)
            maxSum = max(lSum, rSum, lPath+root.val+rPath, maxPath)
            return maxSum, maxPath
