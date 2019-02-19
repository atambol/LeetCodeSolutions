class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case
        l = len(nums)
        if l <= 2:
            nums.reverse()
            return
        
        
        # find the first decreasing position from left
        i = l-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        # nums is largest
        if i < 0:
            nums.reverse()
        else:
            # find the next position greater than nums[i]
            pos = i + 1
            j = pos
            while j <= l-1:
                if nums[pos] >= nums[j] > nums[i] :
                    pos = j
                j += 1
            
            # exchange i and pos
            nums[i], nums[pos] = nums[pos], nums[i]
            
            # reverse nums[i+1:]
            i = min(i+1, l-1)
            j = l-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
