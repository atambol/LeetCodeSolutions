# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        node = root
        parent = None
        while node and node.val != p.val:
            if node.val < p.val:
                node = node.right
            else:
                parent = node
                node = node.left
                
        if not node.right:
            return parent
        else:
            node = node.right
            
            while node.left:
                node = node.left
            return node
