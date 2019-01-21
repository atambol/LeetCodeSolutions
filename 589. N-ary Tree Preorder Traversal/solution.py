"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        sol = []
        
        # edge case
        if not root:
            return sol
        
        # visit root
        sol.append(root.val)
        
        # visit children
        for child in root.children:
            sol.extend(self.preorder(child))
            
        return sol
