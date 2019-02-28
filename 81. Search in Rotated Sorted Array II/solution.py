class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.mysearch(nums, target, 0, len(nums)-1)
        
    def mysearch(self, nums, target, low, high):
        # base case
        if high - low <= 1:
            return target in nums[low:high+1]
        
        # check mid
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        
        # check if there is repetition -> tends to O(n) solution
        if nums[low] == nums[high] or nums[mid] == nums[high]:
            return self.mysearch(nums, target, low, mid-1) or self.mysearch(nums, target, mid+1, high)
        
        # look for the sorted side and choose the correct half
        elif nums[mid] < nums[high]:
            if nums[mid] < target <= nums[high]:
                return self.mysearch(nums, target, mid+1, high)
            else:
                return self.mysearch(nums, target, low, mid-1)
        else:
            if nums[low] <= target < nums[mid]:
                return self.mysearch(nums, target, low, mid-1)
            else:
                return self.mysearch(nums, target, mid+1, high)
                
        
