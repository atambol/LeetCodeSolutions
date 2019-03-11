# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # reach the node
        parent = None
        node = root
        while node and node.val != p.val:
            if node.val > p.val:
                parent = node
                node = node.left
            else:
                node = node.right
                
        # get the successor
        if node.right:
            node = node.right
            while node.left:
                node = node.left
                
            return node
        else:
            return parent
