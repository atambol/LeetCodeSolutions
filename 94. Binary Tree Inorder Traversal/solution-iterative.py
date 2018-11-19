# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        inorder = []
        
        node = root
        while node or stack:
            if node:
                # if the node exists, insert it to the stack and go to its left node
                stack.append(node)
                node = node.left
            else:
                # node is empty, pop the last element pushed to the stack, 
                # store its value and go to its right child
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
                
        return inorder
            
            
