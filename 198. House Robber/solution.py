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
        loot = [0]*len(nums)
        for i in range(len(nums)):
            if i - 2 >= 0:
                loot1 = loot[i-2]
            else:
                loot1 = 0
            
            if i - 3 >= 0:
                loot2 = loot[i-3]
            else:
                loot2 = 0                
                
            loot[i] = max(nums[i] + loot1, nums[i] + loot2)
            
        return max(loot[-1], loot[-2])
        
