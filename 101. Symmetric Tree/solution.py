# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.myIsSymmetric(root.left, root.right)
        
    def myIsSymmetric(self, left, right):
        if not left and not right:
            return True
        if not right and left:
            return False
        if right and not left:
            return False
        
        if left.val == right.val:
            return  self.myIsSymmetric(left.left, right.right) and \
                    self.myIsSymmetric(right.left, left.right)
        else:
            return False
