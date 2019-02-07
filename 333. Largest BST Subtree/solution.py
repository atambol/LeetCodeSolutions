# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        
        count, _, _, _ = self.myLargestBSTSubtree(root)
        return count
        
    def myLargestBSTSubtree(self, root):
        if root.left and root.right:
            lcount, lnode, lmin, lmax = self.myLargestBSTSubtree(root.left)
            rcount, rnode, rmin, rmax = self.myLargestBSTSubtree(root.right)
            if lnode == root.left and rnode == root.right and lmax < root.val < rmin:
                    return 1 + lcount + rcount, root, lmin, rmax
            elif lcount > rcount:
                return lcount, lnode, lmin, lmax
            else:
                return rcount, rnode, rmin, rmax
        elif not root.left and root.right:
            rcount, rnode, rmin, rmax = self.myLargestBSTSubtree(root.right)
            if rnode == root.right and root.val < rmin:
                return 1 + rcount, root, root.val, rmax
            else:
                return rcount, rnode, rmin, rmax
        elif root.left and not root.right:
            lcount, lnode, lmin, lmax = self.myLargestBSTSubtree(root.left)
            if lnode == root.left and lmax < root.val:
                return 1 + lcount, root, lmin, root.val
            else:
                return lcount, lnode, lmin, lmax
        else:
            return 1, root, root.val, root.val
