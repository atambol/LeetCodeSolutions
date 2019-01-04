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
        return max(self.myrob(root))
        
    def myrob(self, root):
        if not root:
            return 0, 0
        
        if root.left:
            wleft, woleft = self.myrob(root.left)
        else:
            wleft, woleft = 0, 0
            
        if root.right:
            wright, woright = self.myrob(root.right)
        else:
            wright, woright = 0, 0        
            
        # loot with root
        wroot = root.val + woleft + woright
        
        # loot without root
        woroot = max(wleft+wright, wleft+woright, woleft+wright, woleft+woright)
        
        return wroot, woroot
            
