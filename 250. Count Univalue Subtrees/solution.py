# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a, b = self.myCountUnivalSubtrees(root)
        return a
        
        
    def myCountUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int int
        """
        if not root:
            return 0, None
        
        lcount, lval = self.myCountUnivalSubtrees(root.left)
        rcount, rval = self.myCountUnivalSubtrees(root.right)
        
        mycount = lcount + rcount
        if (lval == None or root.val == lval) and (rval == None or root.val == rval):
            mycount += 1
            return mycount, root.val
        else:
            return mycount, sys.maxsize
        
            
