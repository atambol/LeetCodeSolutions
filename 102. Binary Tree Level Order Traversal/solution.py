# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        sol = []
        if not root:
            return sol
        
        queue = [root]
        while queue:
            level = []
            newqueue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            sol.append(level)
            queue = newqueue
            
            return sol
