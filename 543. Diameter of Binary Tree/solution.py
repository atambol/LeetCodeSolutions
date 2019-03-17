# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        dep, dia = self.getD(root)
        return dia-1
        
    def getD(self, root):
        if not root:
            return 0, 0
        
        ldep, ldia = self.getD(root.left)
        rdep, rdia = self.getD(root.right)
        return max(ldep, rdep) + 1, max(ldia, rdia, ldep + rdep + 1)
    
