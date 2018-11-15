# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        
        if root.val > V:
            sol = self.splitBST(root.left, V)
            root.left = sol[1]
            return [sol[0], root]
        else:
            sol = self.splitBST(root.right, V)
            root.right = sol[0]
            return [root, sol[1]]
            
            
