# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # edge case
        if not root:
            return 0
        
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        
        if left == right:
            return 2 ** left + self.countNodes(root.right)
        else:
            return 2 ** right + self.countNodes(root.left)
        
    def getDepth(self, root):
        d = 0
        while root:
            root = root.left
            d += 1
            
        return d
