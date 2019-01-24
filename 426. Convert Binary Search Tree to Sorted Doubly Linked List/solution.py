"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # edge cases
        if not root:
            return root
        
        # transform and get the edge nodes
        left, right = self.transform(root)
        
        # tie up the edges
        left.left = right
        right.right = left
        
        # return head
        return left

        
    def transform(self, root):
        # both children present
        if root.left and root.right:
            left1, left2 = self.transform(root.left)
            right1, right2 = self.transform(root.right)
            left2.right = root
            root.left = left2
            right1.left = root
            root.right = right1
            return left1, right2
        
        # only left
        elif root.left and not root.right:
            left1, left2 = self.transform(root.left)
            left2.right = root
            root.left = left2
            return left1, root
        
        # only right
        elif not root.left and root.right:
            right1, right2 = self.transform(root.right)
            right1.left = root
            root.right = right1
            return root, right2
        
        # childless
        else:
            return root, root
