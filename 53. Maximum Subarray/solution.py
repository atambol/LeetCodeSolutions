class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if not nums:
            return None
        
        # two sum variables
        maxSum = nums[0]
        curSum = nums[0]
        
        for num in nums[1:]:
            curSum = max(curSum+num, num)
            maxSum = max(maxSum, curSum)
            
        return maxSum
