# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_dia, max_len = self.mydiameterOfBinaryTree(root)
        return max_dia
    
    def mydiameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Leaf node condition
        if not root.left and not root.right:
            return 0, 0
        else:
            left_len = 0
            left_dia = 0
            if root.left:
                left_dia, left_len = self.mydiameterOfBinaryTree(root.left)
                
            right_len = 0
            right_dia = 0
            if root.right:
                right_dia, right_len = self.mydiameterOfBinaryTree(root.right)
                
            root_dia = 0
            if root.left and root.right:
                root_dia = right_len + left_len + 2
            elif root.left:
                root_dia = left_len + 1
            elif root.right:
                root_dia = right_len + 1

            root_len = max(right_len, left_len) + 1
            root_dia = max(root_dia, left_dia, right_dia)
            
            return root_dia, root_len
