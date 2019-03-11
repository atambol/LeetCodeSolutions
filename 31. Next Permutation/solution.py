class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case
        if len(nums) < 2:
            return 
        
        # look for a decreasing order from right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        # i runs below 0
        if i < 0:
            nums.reverse()
            return
        
        # look for the next largest numbers
        j = i+1
        k = j
        n = nums[j]
        while j < len(nums):
            if n >= nums[j] > nums[i]:
                k = j
                n = nums[j]
            j += 1
            
        # swap and reverse
        nums[i], nums[k] = nums[k], nums[i]
        i = i + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j -= 1
            
