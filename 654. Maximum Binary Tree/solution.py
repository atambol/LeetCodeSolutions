# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        max_num = max(nums)
        max_num_i = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_num_i])
        root.right = self.constructMaximumBinaryTree(nums[max_num_i+1:])
        return root
        
