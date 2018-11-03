# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and q:
            return False
        elif not q and p:
            return False
        elif not q and not p:
            return True
        else:
            if p.val == q.val:
                return  self.isSameTree(p.left, q.left) and \
                        self.isSameTree(p.right, q.right)
            else:
                return False
