class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # edge case
        if k < 2:
            return 0
        
        # using the sliding window technique
        prod = 1
        count = 0
        i = 0
        
        # loop over each set
        for j, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod = prod/nums[i]
                i += 1
            count += j - i + 1
            
        return count
