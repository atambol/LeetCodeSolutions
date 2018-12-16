# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = []
        queue.append(root)
        levelAvg = []
        while queue:
            newqueue = []
            total = 0
            for node in queue:
                total += node.val
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            levelAvg.append(total/len(queue))
            queue = newqueue
        return levelAvg
                    
