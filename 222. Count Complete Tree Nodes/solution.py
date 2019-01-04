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
        if not root:
            return 0
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left == right:
            return 2**left + self.countNodes(root.right)
        else:
            return 2**right + self.countNodes(root.left)
        
    def getHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count
