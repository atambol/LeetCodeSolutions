# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.myUpsideDownBinaryTree(root, None, None)
            
    def myUpsideDownBinaryTree(self, root, right, left):
        if not root:
            return right
        
        myright = root.right
        myleft = root.left
        root.left = left
        root.right = right
        
        return self.myUpsideDownBinaryTree(myleft, root, myright)
        
