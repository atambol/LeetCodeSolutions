# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilts = []
        
        def tilt(node):
            """
            :type root: TreeNode
            :rtype: int, int
            """
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            
            leftSum = tilt(node.left)
            rightSum = tilt(node.right)
            tilts.append(abs(leftSum - rightSum))
            return rightSum + leftSum + node.val
        
        tilt(root)
        return sum(tilts)
