# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # edge case
        if not root:
            return []
        else:
            # check if the node is leaf node
            if not root.left and not root.right:
                # does the path to leaf node satisfy the sum
                if sum == root.val:
                    return [[root.val]]
                else:
                    return []
            else:
                # get paths from left and right subtree
                left = self.pathSum(root.left, sum-root.val)
                right = self.pathSum(root.right, sum-root.val)
                mypaths = []
                
                # prepend root's val to these paths
                for x in left + right:
                    mypaths.append([root.val] + x)
                    
                return mypaths
