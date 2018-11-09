class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def binSearch(nums, i, j):
            # Base condition
            if abs(i-j) == 1:
                return min(nums[i], nums[j])
            if i == j:
                return nums[i]
            
            # Find the mid point
            mid = (i + j)/2

            # Check for irregularity on either sides on mid
            if nums[mid] > nums[j]:
                return binSearch(nums, mid, j)
            else:
                return binSearch(nums, i, mid)
                    
        return binSearch(nums, 0, len(nums)-1)
        
