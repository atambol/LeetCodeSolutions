class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sol = [0]*len(nums)
        sol[0] = nums[0]
        sol[1] = nums[1]
        
        for i in range(2, len(nums)):
            sol[i] = max(sol[i-3], sol[i-2]) + nums[i]
            
        return max(sol[-1], sol[-2])
