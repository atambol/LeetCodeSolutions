# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        path, max = self.myPathSum(root)
        return max
        
    def myPathSum(self, root):
        if root.left and root.right:
            lpath, lmax = self.myPathSum(root.left)
            rpath, rmax = self.myPathSum(root.right)
            maxCand = [lmax, rmax, lpath, rpath, lpath+root.val, rpath+root.val, root.val, lpath+root.val+rpath]
            pathCand = [lpath+root.val, rpath+root.val, root.val]
            return max(pathCand), max(maxCand)
        elif root.left and not root.right:
            lpath, lmax = self.myPathSum(root.left)
            maxCand = [lmax, lpath, lpath+root.val, root.val]
            pathCand = [lpath+root.val, root.val]
            return max(pathCand), max(maxCand)
        elif not root.left and root.right:
            rpath, rmax = self.myPathSum(root.right)
            maxCand = [rmax, rpath, rpath+root.val, root.val]
            pathCand = [rpath+root.val, root.val]
            return max(pathCand), max(maxCand)
        else:
            return root.val, root.val
        
    
