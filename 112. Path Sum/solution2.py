# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # edge case
        if not root:
            return False
        else:
            # check for each case of left and right subtree
            if root.left and root.right:
                left = self.hasPathSum(root.left, sum - root.val)
                right = self.hasPathSum(root.right, sum - root.val)
                return left or right
            elif not root.left and root.right:
                return self.hasPathSum(root.right, sum - root.val)
            elif root.left and not root.right:
                    return self.hasPathSum(root.left, sum - root.val)
            else:
                # final case where root is equal to sum
                if sum == root.val:
                    return True
                else:
                    return False
