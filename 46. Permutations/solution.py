class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        if len(nums) == 2:
            return [
                nums,
                nums[::-1]
            ]
            
        sol = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] +  nums[i+1:]):
                sol.append([nums[i]] + p)
                
        return sol
