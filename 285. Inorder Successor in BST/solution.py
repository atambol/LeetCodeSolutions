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
        succ = None
        node = root
        # reach p in O(log n)
        while node != p:
            if node.val > p.val:
                succ = node
                node = node.left
            else:
                node = node.right
        
        # if the node has a right subtree, successor is subtree's left most node
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # if node doesnt have right subtree, successor is succ
        else:
            return succ
