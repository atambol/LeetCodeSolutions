# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        if not root:
            return sol
        
        sol.append(root.val)
        
        # left
        node = root.left
        if node:
            while node:
                sol.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

            sol.pop()
                
        # bottom
        node = root.left
        stack = [root.right]
        while stack or node:
            if node:
                if not node.left and not node.right:
                    sol.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

        
        # right
        node = root.right
        sol2 = []
        if node:
            while node:
                sol2.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left

            sol2.pop()
            sol.extend(sol2[::-1])

        return sol
            
