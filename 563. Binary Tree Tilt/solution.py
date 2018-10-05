# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt, total = self.myTilt(root)
        return tilt
        
    def myTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int, int
        """
        if not root:
            return 0, 0
        leftTilt, leftTotal = self.myTilt(root.left)
        rightTilt, rightTotal = self.myTilt(root.right)
        tilt = abs(leftTotal - rightTotal)
        return leftTilt + tilt + rightTilt, leftTotal + root.val + rightTotal
