# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        preorder = []
        node = root
        
        while node or stack:
            # check the node and print its value
            # push its right child to the stack
            # update the node to its left child
            if node:
                preorder.append(node.val)
                stack.append(node.right)
                node = node.left
            # if the node does not exist, pop from stack 
            else:
                node = stack.pop()
                
        return preorder
                
