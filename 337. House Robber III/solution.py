# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return max(self.traverse(root))
    
    def traverse(self, root):
        if not root:
            return 0,0 
        
        wl, wol = self.traverse(root.left)
        wr, wor = self.traverse(root.right)

        wme = wol + wor + root.val
        wome = max(wol + wor, wl + wr, wor + wl, wr + wol)
        return wme, wome
