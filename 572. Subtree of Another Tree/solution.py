# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s and t:
            if s.val == t.val:
                return self.isReplica(s, t) or \
                self.isSubtree(s.left, t) or \
                self.isSubtree(s.right, t)
            else:
                return self.isSubtree(s.left, t) or \
                self.isSubtree(s.right, t)
        else:
            return False

    def isReplica(self, s, t):
        if not s and not t:
            return True
        if not s and t:
            return False
        if s and not t:
            return False

        if s.val == t.val:
            return True and \
            self.isReplica(s.left, t.left) and \
            self.isReplica(s.right, t.right)
        else:
            return False
