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
        
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        
        # we need to look further right in this case
        if left == right:
            return 2**left + self.countNodes(root.right)
        else:
            return 2**right + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + self.getDepth(root.left)
