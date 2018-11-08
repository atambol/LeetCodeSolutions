# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def rec(node):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if not node:
                return False
            
            left = rec(node.left)
            if not left:
                node.left = None
            right = rec(node.right)
            if not right:
                node.right = None
                
            return left or right or node.val == 1
        
        rec(root)
        return root
