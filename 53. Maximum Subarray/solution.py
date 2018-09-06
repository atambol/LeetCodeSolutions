class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        max_total = nums[0]
        for num in nums[1:]:
            total = max(num, num + total)
            if total > max_total:
                max_total = total
                
        return max_total
