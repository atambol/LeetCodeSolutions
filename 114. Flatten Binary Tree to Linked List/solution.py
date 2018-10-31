# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        self.attach(root.left, root.right)
        if root.left:
            root.right = root.left
            root.left = None
        
        
    def attach(self, root, subtree):
        if root:
            if not root.right:
                root.right = subtree
            else:
                self.attach(root.right, subtree)
