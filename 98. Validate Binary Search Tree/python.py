# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        return self.validate(root, -sys.maxsize-1, sys.maxsize)
        
    def validate(self, root, low, high):
        if not root:
            return True
        else:
            if low < root.val < high:
                return self.validate(root.left, low, root.val) and self.validate(root.right, root.val, high)
            else:
                return False
            
