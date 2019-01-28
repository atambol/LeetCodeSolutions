# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return sys.maxsize
        
        if target == root.val:
            return root.val
        else:
            diff1 = abs(root.val - target)
            if target > root.val:
                val = self.closestValue(root.right, target)
            else:
                val = self.closestValue(root.left, target)
                
            diff2 = abs(val - target)
            if diff2 > diff1:
                return root.val
            else:
                return val
