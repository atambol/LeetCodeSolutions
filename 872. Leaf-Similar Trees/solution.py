# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        return self.getLeaves(root1) == self.getLeaves(root2)
    
    def getLeaves(self, root):
        if not root:
            return ""
        
        if not root.left and not root.right:
            return str(root.val)
        else:
            return self.getLeaves(root.left) + self.getLeaves(root.right)
