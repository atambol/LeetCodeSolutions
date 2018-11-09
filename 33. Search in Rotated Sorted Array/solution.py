class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        def binSearch(nums, i, j):
            nonlocal target
            
            # Base condition 1
            if abs(i-j) == 1:
                print()
                if target == nums[i]:
                    return i
                elif target == nums[j]:
                    return j
                else:
                    return -1

            # Base condition 2
            if i == j:
                if target == nums[i]:
                    return i
                else:
                    return -1
            
            # Find the mid point
            mid = (i + j)//2

            # Check for irregularity on either sides on mid
            if nums[mid] <= nums[j]:
                if nums[mid] <= target and target <= nums[j]:
                    return binSearch(nums, mid, j)
                else:
                    return binSearch(nums, i, mid)
            else:
                if nums[i] <= target and target <= nums[mid]:
                    return binSearch(nums, i, mid)
                else:
                    return binSearch(nums, mid, j)
                    
        return binSearch(nums, 0, len(nums)-1)

            
