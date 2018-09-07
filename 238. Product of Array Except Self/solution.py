class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        lproduct = [0]*len(nums)
        lproduct[0] = 1
        for i in range(1, len(nums)):
            lproduct[i] = lproduct[i-1] * nums[i-1]
            
        rproduct = 1
        for i in range(len(nums)-2, -1, -1):
            rproduct *= nums[i+1]
            lproduct[i] = lproduct[i] * rproduct
            
        return lproduct
