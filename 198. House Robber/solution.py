class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge cases
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        # loot will be calculated bottom up using dynamic programming
        loot1 = 0 # loot one cell behind
        loot2 = 0 # loot two cells behind
        for i in range(len(nums)):
            loot = max(loot1, nums[i] + loot2)
            loot2, loot1 = loot1, loot
            
        return loot1
        
