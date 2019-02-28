# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if left == right:
            return self.countNodes(root.right) + 2**left
        else:
            return self.countNodes(root.left) + 2**right
        
    def getDepth(self, node):
        if not node:
            return 0
        
        count = 0
        while node:
            count += 1
            node = node.left
            
        return count
