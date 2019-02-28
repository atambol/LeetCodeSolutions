# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        x, y = self.inorder(root, k)
        return x
    
    def inorder(self, root, k):
        if not root:
            return None, k
        
        left, k = self.inorder(root.left, k)
        if not k:
            return left, k
        k-=1
        if not k:
            return root.val, k
        
        return self.inorder(root.right, k)
