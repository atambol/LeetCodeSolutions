# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # edge cases
        if not inorder:
            return None
        
        # the first node in preorder is root and obtain its index of in inorder
        root = TreeNode(preorder[0])
        indexOfRoot = inorder.index(root.val)
        
        # get the length of inorder and preorder array to operate on for left and right subtree
        root.left = self.buildTree(preorder[1:1+indexOfRoot], inorder[:indexOfRoot])
        root.right = self.buildTree(preorder[1+indexOfRoot:], inorder[indexOfRoot+1:])
        
        # return the root
        return root
        
