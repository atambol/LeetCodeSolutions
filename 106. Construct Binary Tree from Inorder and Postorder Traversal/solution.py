# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # edge cases
        if not inorder:
            return None
        
        # the first node in preorder is root and obtain its index in inorder
        root = TreeNode(postorder[-1])
        indexOfRoot = inorder.index(root.val)
        
        # get the length of inorder and postorder array to operate on for left and right subtree
        root.left = self.buildTree(inorder[:indexOfRoot], postorder[:indexOfRoot])
        root.right = self.buildTree(inorder[indexOfRoot+1:], postorder[indexOfRoot:-1])
        
        # return the root
        return root
