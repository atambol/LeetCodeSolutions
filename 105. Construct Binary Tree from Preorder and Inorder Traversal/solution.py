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

        if not preorder:
            return None

        root = TreeNode(preorder[0]) 
        index = self.getIndex(inorder, root.val)
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
    
    def getIndex(self, inorder, val):
        if inorder == None:
            return -1
        for i in range(len(inorder)):
            if inorder[i] == val:
                return i
        return -1
