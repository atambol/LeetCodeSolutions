# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, root):
        if not root:
            return 
        
        self.inorder(root.left)
        if self.prev:
            if self.prev.val > root.val:
                if self.first:
                    self.second = root
                else:
                    self.first = self.prev
                    self.second = root
        self.prev = root
        self.inorder(root.right)
        
        
            
