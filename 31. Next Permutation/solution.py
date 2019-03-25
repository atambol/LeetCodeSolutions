class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case
        if len(nums) < 2:
            return
        
        # find first decreasing order from right
        n = len(nums) - 1
        i = n-1
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
            
        if i == -1:
            nums.reverse()
            return
        
        # look for smallest number larger than nums[i] from i to right
        k = i+1
        for j in range(i+2, n+1):
            if nums[k] >= nums[j] > nums[i]:
                k = j
                
        # exchange and reverse
        nums[k], nums[i] = nums[i], nums[k]
        i += 1
        j = n
        while i < j:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            j -= 1
