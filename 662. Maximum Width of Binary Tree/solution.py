# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0)]
        width = 0
        while queue:
            newqueue = []
            ws = []
            for node, w in queue:
                if node.left:
                    newqueue.append((node.left, 2*w))
                if node.right:
                    newqueue.append((node.right, 2*w+1))
                ws.append(w)
            queue = newqueue
            width = max(width, max(ws) - min(ws) + 1)
        return width
            
