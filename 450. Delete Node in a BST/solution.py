# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        # if current node is to be removed
        if root.val == key:
            left = root.left
            right = root.right
            
            # the right subtree is empty, just attach the left subtree as it is
            if not right:
                return left
            else:
                # find the left most empty node on the right subtree
                if right.left:
                    root = right.left
                    while root and root.left:
                        root = root.left
                    root.left = left
                else:
                    right.left = left
                return right
            
        # look on the left side 
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        
        # look on the right side
        else:
            root.right = self.deleteNode(root.right, key)
            return root
