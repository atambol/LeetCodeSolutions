class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # mark indices with -ve sign if the element is found
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # look for positive elements to get missing elements
        sol = []
        for i, num in enumerate(nums):
            if num > 0:
                sol.append(i+1)
                
        return sol
