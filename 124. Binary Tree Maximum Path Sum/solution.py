# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MaxPath, lMaxSum = self.myMaxPathSum(root)
        return lMaxSum
        
    def myMaxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int, int
        """
        if root.left and root.right:
            lMaxPath, lMaxSum = self.myMaxPathSum(root.left)
            rMaxPath, rMaxSum = self.myMaxPathSum(root.right)
            possibleSums = [
                            root.val + lMaxPath + rMaxPath, # self, right and left
                            root.val + lMaxPath, # self and left
                            root.val + rMaxPath, # self and right
                            lMaxSum, # left only
                            rMaxSum, # right only
                            root.val # self only
                           ]
            possiblePaths = [rMaxPath + root.val, lMaxPath + root.val, root.val]
            return max(possiblePaths), max(possibleSums)
        elif root.left and not root.right:
            lMaxPath, lMaxSum = self.myMaxPathSum(root.left)
            possibleSums = [
                            root.val + lMaxPath, # self and left
                            lMaxSum, # left only
                            root.val # self only
                           ]
            possiblePaths = [lMaxPath + root.val, root.val]
            return max(possiblePaths), max(possibleSums)
        elif not root.left and root.right:
            rMaxPath, rMaxSum = self.myMaxPathSum(root.right)
            possibleSums = [
                            root.val + rMaxPath, # self and right
                            rMaxSum, # right only
                            root.val # self only
                           ]
            possiblePaths = [rMaxPath + root.val, root.val]
            return max(possiblePaths), max(possibleSums)
        else:
            return root.val, root.val
                
