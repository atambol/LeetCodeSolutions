class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
            
        rob1 = self.myrob(nums[:-1])
        rob2 = self.myrob(nums[1:])
        return max(rob1, rob2)
        
    def myrob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        
        p1 = nums[0]
        p2 = nums[1]
        p3 = nums[2] + p1
        
        for num in nums[3:]:
            p3, p2, p1 = num + max(p1, p2), p3, p2
            
        return max(p3, p2)
