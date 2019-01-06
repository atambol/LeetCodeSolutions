class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # edge cases
        n = len(nums)
        if not n:
            return 0
        
        if k < 2:
            return 0
        
        # two pointers
        i = 0 
        j = 0
        prod = 1
        count = 0
        
        while j < n:
            prod *= nums[j]
            while prod >= k:
                prod /= nums[i]
                i += 1
            count += j - i + 1
            j += 1
            
        return count
            
