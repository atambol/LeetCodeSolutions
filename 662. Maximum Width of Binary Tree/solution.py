# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
        # edge cases
        if not root:
            return 0
        
        # create a queue
        queue = [(root, 0)]
        width = 0
        
        # level order traversal
        while queue:
            # calculate positions of nodes
            newqueue = []
            positions = []
            for node, pos in queue:
                if node.left:
                    newqueue.append((node.left, pos*2))
                if node.right:
                    newqueue.append((node.right, pos*2+1))
                positions.append(pos)

            # calculate width
            width = max(width, max(positions)-min(positions) + 1)
            queue = newqueue
        return width
