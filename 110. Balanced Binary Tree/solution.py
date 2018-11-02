# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, height = self.myIsBalanced(root)
        return balanced
    
    def myIsBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool, int
        """
        if not root:
            return True, 0
        else:
            lbal, lht = self.myIsBalanced(root.left)
            rbal, rht = self.myIsBalanced(root.right)
            mybal = (abs(lht - rht) <= 1) and lbal and rbal
            myht = 1 + max(lht, rht)
            return mybal, myht
        
