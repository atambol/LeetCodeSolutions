# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # edge cases
        if not root or (not root.left and not root.right):
            return 0
        
        x, y = self.mySumOfLeftLeaves(root)
        return x

    def mySumOfLeftLeaves(self, root):
        # edge case
        if not root:
            return 0, False
        
        # found a leaf node
        if not root.left and not root.right:
            return root.val, True
        
        # check left and right
        lval, lcond = self.mySumOfLeftLeaves(root.left)
        rval, rcond = self.mySumOfLeftLeaves(root.right)
        
        # if right node is not leaf, add its contribution
        if not rcond:
            return lval + rval, False
        # add contribution of left always
        else:
            return lval, False
                
            
