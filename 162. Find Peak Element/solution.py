class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary search to find peak
        def recur(nums, i, j):
            if i == j:
                return i
        
            if i + 1 == j:
                return i if nums[i] > nums[j] else j
        
            mid = (i + j) // 2
            if nums[mid] < nums[mid+1]:
                return recur(nums, mid, j)
            else:
                return recur(nums, i, mid)
            
            
        return recur(nums, 0, len(nums)-1)
