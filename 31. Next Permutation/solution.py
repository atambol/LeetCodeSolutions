class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case
        if not nums:
            return
        
        # find the first decreasing order from left
        n = len(nums) - 1
        i = n-1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        # edge case - nums is largest
        if i < 0:
            nums.reverse()
            return
        
        # find the next just largest number to nums[i]
        j = i + 1
        k = i
        maxNum = sys.maxsize
        while j <= n:
            if nums[j] > nums[i] and nums[j] <= maxNum:
                maxNum = nums[j]
                k = j
            j += 1
            
        # exchange the numbers
        nums[i], nums[k] = nums[k], nums[i]
        
        # reverse the numbers i onwards
        i = i+1
        j = n
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
