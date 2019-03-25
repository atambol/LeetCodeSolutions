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
        
        return max(self.myRob(root))
        
    def myRob(self, root):
        if not root:
            return 0, 0
        
        wl, wol = self.myRob(root.left)
        wr, wor = self.myRob(root.right)
        
        return root.val + wol + wor, max(wol, wl) + max(wor, wr)
