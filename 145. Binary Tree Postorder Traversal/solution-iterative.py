# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        visited = 1
        visiting = 0
        sol = []
        node = root
        while node or stack:
            if node:
                stack.append((node, visiting))
                node = node.left
            else:
                node, status = stack.pop()
                if status == visiting:
                    stack.append((node, visited))
                    node = node.right
                else:
                    sol.append(node.val)
                    node = None
                    
        return sol
                    
