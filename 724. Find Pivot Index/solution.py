class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        sumLeft = [0]*len(nums)
        sumRight = [0]*len(nums)
        
        # find sum of elements starting from left side of array
        for i in range(len(nums)):
            try:
                sumLeft[i] = sumLeft[i-1] + nums[i]
            except IndexError:
                sumLeft[i] = nums[i]
        
        # find sum of elements starting from right side of array
        for i in range(len(nums)-1, -1, -1):
            try:
                sumRight[i] = sumRight[i+1] + nums[i]
            except IndexError:
                sumRight[i] = nums[i]        
                
        # find the point where sum is the same
        for i in range(len(nums)):
            if sumRight[i] == sumLeft[i]:
                return i
            
        return -1
