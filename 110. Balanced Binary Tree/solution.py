# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        height, balanced = self.getHeight(root)
        return balanced
        
    def getHeight(self, root):
        if root:
            leftH, leftBalanced = self.getHeight(root.left)
            rightH, rightBalanced = self.getHeight(root.right)
            balanced = leftBalanced and rightBalanced
            if not balanced:
                return 0, False   # No need to waste time in calculating height if children are unbalanced
            if abs(leftH - rightH) > 1:
                return 0, False   # No need to waste time in calculating height if children are unbalanced
            else:
                return 1 + max(leftH, rightH), balanced
        else:
            return 0, True
