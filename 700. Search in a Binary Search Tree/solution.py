# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right
                
        return None
