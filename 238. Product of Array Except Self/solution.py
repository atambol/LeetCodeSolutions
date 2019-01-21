class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # edge cases
        if not nums: 
            return nums
        
        # calculate product from left
        prev = nums[0]
        left = [1]
        
        for num in nums[1:]:
            left.append(prev)
            prev *= num
        
        # calculate product from right
        prev = nums[-1]
        right = [1]
        
        for num in nums[-2::-1]:
            right.append(prev)
            prev *= num
            
        right.reverse()
        
        # calculate final sol
        sol = []
        for l, r in zip(left, right):
            sol.append(l*r)

        return sol
