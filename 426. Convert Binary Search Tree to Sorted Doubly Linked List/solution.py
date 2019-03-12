"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        left, right = self.convert(root)
        left.left = right
        right.right = left
        return left
        
    def convert(self, root):
        if not root.left and not root.right:
            return root, root
        elif root.left and not root.right:
            left, right = self.convert(root.left)
            right.right = root
            root.left = right
            return left, root
        elif root.right and not root.left:
            left, right = self.convert(root.right)
            left.left = root
            root.right = left
            return root, right
        else:
            lleft, lright = self.convert(root.left)
            rleft, rright = self.convert(root.right)
            lright.right = root
            root.left = lright
            rleft.left = root
            root.right = rleft
            return lleft, rright
