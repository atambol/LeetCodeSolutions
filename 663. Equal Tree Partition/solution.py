# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        
        stack = []
        node = root
        total = 0
        
        while node or stack:
            if node:
                total += node.val
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        
        if total%2 == 1:
            return False
        
        half = total/2
        _, status = self.dfs(root, half)
        return status
    
    def dfs(self, root, target):
        if root.left and root.right:
            left, status = self.dfs(root.left, target)
            if status:
                return None, status
            right, status = self.dfs(root.right, target)
            if status:
                return None, status
            if left == target or right == target:
                return None, True
            else:
                return left + right + root.val, False
        elif not root.left and root.right:
            right, status = self.dfs(root.right, target)
            if status:
                return None, status
            if right == target:
                return None, True  
            else:
                return root.val + right, False
        elif root.left and not root.right:
            left, status = self.dfs(root.left, target)
            if status:
                return None, status
            if left == target:
                return None, True 
            else:
                return root.val + left, False
        else:
            return root.val, False
            
