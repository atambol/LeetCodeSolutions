class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 1
        sol = []
        
        # start from left, go right and calculate product of prev elements
        for num in nums:
            sol.append(prev)
            prev *= num
            
        # start from right and go left calculating the product
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            sol[i] *= prev
            prev *= nums[i]
    
        return sol
            
        
