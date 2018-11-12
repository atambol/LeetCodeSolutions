# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        maxVal = sys.maxsize
        minVal = -1 - sys.maxsize
        return self.myIsValidBST(root, maxVal, minVal)
        
    def myIsValidBST(self, root, maxVal, minVal):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            if minVal < root.val < maxVal:
                return self.myIsValidBST(root.left, root.val, minVal) and \
                        self.myIsValidBST(root.right, maxVal, root.val) 
            else:
                return False
