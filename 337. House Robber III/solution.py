# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.myRob(root))
    
    def myRob(self, root):
        if not root:
            return 0, 0
        
        # check left and right subtree
        leftInc, leftExc = self.myRob(root.left)
        rightInc, rightExc = self.myRob(root.right)
        
        # 4 cases are possible if root is not included
        return root.val + leftExc + rightExc, max(leftInc + rightInc, leftExc + rightExc, leftExc + rightInc, leftInc + rightExc)
        
