class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums)-1, len(nums)-k)
        
    def quickselect(self, nums, low, high, k):
        if low == high:
            return nums[low]
        
        pivot = nums[low]
        i = low
        j = i + 1
        while j <= high:
            if nums[j] < pivot:
                nums[j], nums[i], i = nums[i+1], nums[j], i + 1
            j += 1
            
        nums[i] = pivot
        if i == k:
            return pivot
        elif i < k:
            return self.quickselect(nums, i+1, high, k)
        else:
            return self.quickselect(nums, low, i-1, k)
        
