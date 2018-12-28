# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.myLongestUnivaluePath(root))
        
    def myLongestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int, int
        """
        if not root:
            return 0, 0
        lcount, lmax = self.myLongestUnivaluePath(root.left)
        rcount, rmax = self.myLongestUnivaluePath(root.right)
        mycount = 0
        mymax = 0
        if root.left and root.right and root.val == root.left.val == root.right.val:
            mymax = lcount + rcount + 2
            mycount = max(lcount, rcount) + 1
        elif root.right and root.val == root.right.val:
            mycount = rcount + 1
            mymax = rcount + 1
        elif root.left and root.left.val == root.val:
            mycount = lcount + 1
            mymax = lcount + 1
        else:
            mycount = 0
            mymax = 0
        return mycount, max(mymax, lmax, rmax)
