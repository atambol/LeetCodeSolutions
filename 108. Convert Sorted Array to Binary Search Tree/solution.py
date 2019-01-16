# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.mySortedArrayToBST(nums, 0, len(nums)-1)
        
    def mySortedArrayToBST(self, nums, i, j):
        if i == j:
            return TreeNode(nums[i])
        
        if i == j - 1:
            root = TreeNode(nums[j])
            root.left = TreeNode(nums[i])
            return root
        
        mid = i + (j - i + 1)//2
        root = TreeNode(nums[mid])
        root.left = self.mySortedArrayToBST(nums, i, mid - 1)
        root.right = self.mySortedArrayToBST(nums, mid + 1, j)
        return root
