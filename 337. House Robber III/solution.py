# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.myRob(root))
        
    def myRob(self, root):
        if root.left and root.right:
            wl, wol = self.myRob(root.left)
            wr, wor = self.myRob(root.right)
            return root.val + wol + wor, max(wr + wol, wl+wor, wl+wr, wor+wol)
        elif root.left and not root.right:
            wl, wol = self.myRob(root.left)
            return root.val + wol, max(wol, wl)
        elif root.right and not root.left:
            wr, wor = self.myRob(root.right)
            return root.val + wor, max(wor, wr)
        else:
            return root.val, 0
