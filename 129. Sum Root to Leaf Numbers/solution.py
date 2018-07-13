# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        nums = self.dfs(root.left, root.val) + self.dfs(root.right, root.val) 
        sum = 0
        for num in nums:
            sum += num
        return sum
        
    def dfs(self, root, val):
        if not root:
            return []
        newval = val * 10 + root.val
        if not root.left and not root.right:
            return [newval]
        if root.right and not root.left:
            return self.dfs(root.right, newval)
        elif root.left and not root.right:
            return self.dfs(root.left, newval)
        elif root.right and root.left:
            return self.dfs(root.left, newval) + self.dfs(root.right, newval)
        
