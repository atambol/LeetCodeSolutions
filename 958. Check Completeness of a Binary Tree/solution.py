# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        empty = False
        while queue:
            newqueue = []
            for node in queue:
                if node == None:
                    empty = True
                else:
                    if empty:
                        return False
                    newqueue.append(node.left)
                    newqueue.append(node.right)

            queue = newqueue
        return True
        
