# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base condition
        if root == None:
            return None
        
        # Check the left and right subtree 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If the LCA is already found, pass it on as such
        if left not in (None, p, q):
            return left
        if right not in (None, p, q):
            return right
        
        # If the LCA is not found, check the situation at this node
        found_p = p in [root, left, right]
        found_q = q in [root, left, right]
        
        if found_p and found_q:
            return root
        elif found_p:
            return p
        elif found_q:
            return q
        else:
            return None
