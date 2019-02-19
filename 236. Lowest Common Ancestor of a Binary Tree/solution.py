# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lca, _ = self.LCA(root, p, q)
        return lca
        
    def LCA(self, root, p, q):
        if not root:
            return None, False
        
        # look left and right
        left, lstatus = self.LCA(root.left, p, q)
        right, rstatus = self.LCA(root.right, p, q)
        
        # if already found, pass along
        if lstatus:
            return left, lstatus
        if rstatus:
            return right, rstatus
        
        # check if p and q found in this subtree
        cand = set([left, right, root])
        if p in cand and q in cand:
            return root, True
        elif (p in cand and not q in cand):
            return p, False
        elif not p in cand and q in cand:
            return q, False
        else:
            return None, False
