class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Mutliply a number at that index with -1
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            if nums[index] > 0:
                nums[index] *= -1
        
        # Any number at index i that is not negative will be in solution
        res = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                res.append(i+1)
                
        return res
