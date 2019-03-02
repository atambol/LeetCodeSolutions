class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if not nums:
            return 0
        
        running_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            running_sum = max(num, running_sum+num)
            max_sum = max(max_sum, running_sum)
            
        return max_sum
