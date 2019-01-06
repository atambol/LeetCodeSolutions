class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # edge cases
        if not nums:
            return -1
        
        i = 0
        j = len(nums) - 1
        
        while j-i+1 > 3:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[j]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if nums[mid] > target >= nums[i]:
                    j = mid - 1
                else:
                    i = mid + 1
                
            
        for k in range(i, j+1):
            if nums[k] == target:
                return k
            
        return -1
        
        
