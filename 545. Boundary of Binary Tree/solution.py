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
        boundary = []
        if not root:
            return boundary
        
        # add root
        boundary.append(root.val)
        
        # add left side
        node = root.left
        while node:
            boundary.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
                
        if len(boundary) > 1:
            boundary.pop()
        
        # add the bottom
        stack = [root.right]
        preorder = []
        node = root.left
        while node or stack:
            if node:
                if not node.left and not node.right:
                    boundary.append(node.val)
                    node = None
                else:
                    stack.append(node.right)
                    node = node.left
            else:
                node = stack.pop()
        
        # add the right side
        sol = []
        node = root.right
        while node:
            sol.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        if sol:
            sol.pop()
        sol.reverse()
        boundary.extend(sol)
        
        return boundary
