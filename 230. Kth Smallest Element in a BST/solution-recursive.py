# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.k = 0
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        return self.inorder(root)
        
    def inorder(self, root):
        if not root:
            return None
        
        val = self.inorder(root.left)
        if val != None:
            return val
        
        self.k -= 1
        if not self.k:
            return root.val
        
        return self.inorder(root.right)
        
        
        
