# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # perform inorder traversal on the BST, append nodes instead of values
        stack = []
        inorder = []
        
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inorder.append(node)
                node = node.right
        
        # create a skewed tree for each node
        root = TreeNode(None)
        ptr = root
        for node in inorder:
            node.left = None
            ptr.right = node
            ptr = ptr.right
        
        # tie loose ends
        ptr.right = None
        
        return root.right
                
