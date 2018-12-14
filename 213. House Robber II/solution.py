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
        
        return max(self.linearRob(nums[1:]), self.linearRob(nums[:-1]))
        
    def linearRob(self, nums):
        # loot will be calculated bottom up using dynamic programming
        loot1 = 0   # loot one cell back
        loot2 = 0   # loot two cells back
        for i in range(len(nums)):
            loot = max(loot1, loot2+nums[i]) # max loot in current cell
            loot2, loot1 = loot1, loot
            
        return loot1
