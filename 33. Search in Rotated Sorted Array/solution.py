class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        
        return self.mySearch(nums, target, i, j)
    
    def mySearch(self, nums, target, i, j):
        if j - i <= 2:
            while i <= j:
                if target == nums[i]:
                    return i
                i += 1
            
            return -1
        
        mid = (i + j)//2
        if nums[mid] == target:
            return mid
        else:
            if nums[i] < nums[mid]:
                if nums[i] <= target < nums[mid]:
                    return self.mySearch(nums, target, i, mid-1)
                else:
                    return self.mySearch(nums, target, mid+1, j)
            else:
                if nums[mid] < target <= nums[j]:
                    return self.mySearch(nums, target, mid+1, j)
                else:
                    return self.mySearch(nums, target, i, mid-1)
            
