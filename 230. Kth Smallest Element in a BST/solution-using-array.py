# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        sol = []
        
        def myKthSmallest(node, count, k):
            # no need to count beyond k
            if count > k:
                return count
            
            # base condition
            if not node:
                return count
            
            # count the left subtree
            count = myKthSmallest(node.left, count, k)
            
            # count self and check
            if count + 1 == k:
                sol.append(node.val)
                return count + 1
            
            # count right subtree
            count = myKthSmallest(node.right, count + 1,  k)
            return count
        
        myKthSmallest(root, 0, k)
        
        return sol[0]
