# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        total, path = self.getTotal(root)
        return total
    
    def getTotal(self, root):
        if root.left and root.right:
            lsum, lpath = self.getTotal(root.left)
            rsum, rpath = self.getTotal(root.right)
            
            mypath = max(lpath + root.val, rpath + root.val, root.val)
            mysum = max(mypath, rsum, lsum, root.val + lpath + rpath)
            
            return mysum, mypath
        elif not root.left and root.right:
            rsum, rpath = self.getTotal(root.right)
            
            mypath = max(rpath + root.val, root.val)
            mysum = max(mypath, rsum)
            return mysum, mypath
        elif root.left and not root.right:
            lsum, lpath = self.getTotal(root.left)
            
            mypath = max(lpath + root.val, root.val)
            mysum = max(mypath, lsum)
            
            return mysum, mypath
        else:
            return root.val, root.val
