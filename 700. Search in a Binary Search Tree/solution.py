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
        
        if root.val == val:
            return root
        else:
            left = self.searchBST(root.left, val)
            right = self.searchBST(root.right, val)
            if right:
                return right
            elif left:
                return left
            else:
                return None
