# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        width = 0
        queue = [(root, 0)]
        while queue:
            widths = []
            nqueue = []
            for n, w in queue:
                widths.append(w)
                if n.left:
                    nqueue.append((n.left, w*2))
                if n.right:
                    nqueue.append((n.right, w*2 + 1))
                    
            width = max(width, abs(min(widths)-max(widths))+1)
            queue = nqueue
        return width
                    
