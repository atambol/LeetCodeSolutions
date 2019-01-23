# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        succ = None
        while node and node != p:
            if node.val < p.val:
                node = node.right
            else:
                succ = node
                node = node.left
        
        if node and node.right:
            succ = node.right
            while succ.left:
                succ = succ.left
        return succ
