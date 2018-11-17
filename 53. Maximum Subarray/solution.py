class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxSum = nums[0]
        curSum = 0
        for num in nums[1:]:
            curSum = max(num, num+curSum)
            maxSum = max(curSum, maxSum)
            
        return maxSum
