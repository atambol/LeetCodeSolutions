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
        
        return self.mySearch(nums, target, 0, len(nums)-1)
        
    def mySearch(self, nums, target, i, j):
        # base case - length less than equal to 3
        if j-i <= 2:
            for k in range(i, j+1):
                if target == nums[k]:
                    return k
            return -1
        else:
            # check if mid is the target
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            
            # pick the appropriate side
            if nums[mid] < nums[j]:
                if nums[mid] < target <= nums[j]:
                    return self.mySearch(nums, target, mid+1, j)
                else:
                    return self.mySearch(nums, target, i, mid-1)
            else:
                if nums[i] <= target < nums[mid]:
                    return self.mySearch(nums, target, i, mid-1)
                else:
                    return self.mySearch(nums, target, mid+1, j)
