# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.myFlatten(root)
        
    def myFlatten(self, root):
        if not root.right and not root.left:
            return root, root
        elif root.right and not root.left:
            rhead, rtail = self.myFlatten(root.right)
            root.right = rhead
            return root, rtail
        elif not root.right and root.left:
            lhead, ltail = self.myFlatten(root.left)
            root.left = None
            root.right = lhead
            return root, ltail
        else:
            lhead, ltail = self.myFlatten(root.left)
            rhead, rtail = self.myFlatten(root.right)
            root.left = None
            root.right = lhead
            ltail.right = rhead
            return root, rtail
