# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev, minDiff = self.func(root, -sys.maxsize-1, sys.maxsize)
        return minDiff
        
    def func(self, root, prev, minDiff):
        if not root:
            return prev, minDiff
        
        prev, minDiff = self.func(root.left, prev, minDiff)
        if minDiff > abs(root.val - prev):
            minDiff = root.val - prev
        return self.func(root.right, root.val, minDiff)
        
        
