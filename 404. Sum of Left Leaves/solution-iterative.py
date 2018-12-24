# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        sol = 0
        node = root
        while node or stack:
            if node:
                if node.left and not node.left.left and not node.left.right:
                    sol += node.left.val
                    node = node.right
                else:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                node = node.right
                    
        return sol
