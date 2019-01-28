# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        else:
            if root.val > val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    self.insertIntoBST(root.left, val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    self.insertIntoBST(root.right, val)
            return root
