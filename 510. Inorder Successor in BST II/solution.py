"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # check for leftmost node in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # check for the parent who has node as it's left child
        parent = node.parent
        while parent and parent.right == node:
            node = parent
            parent = node.parent
            
        return parent
