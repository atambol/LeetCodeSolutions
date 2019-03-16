class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.mySearch(nums, target, 0, len(nums)-1)
        
    def mySearch(self, nums, target, low, high):
        if low + 1 == high:
            if nums[high] == target:
                return high
            if nums[low] == target:
                return low
            return -1
        elif low == high:
            if nums[low] == target:
                return low
            return -1
        
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[high]:
            if nums[mid] < target <= nums[high]:
                return self.mySearch(nums, target, mid+1, high)
            else:
                return self.mySearch(nums, target, low, mid-1)
        else:
            if nums[low] <= target < nums[mid]:
                return self.mySearch(nums, target, low, mid-1)
            else:
                return self.mySearch(nums, target, mid+1, high) 
