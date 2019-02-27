class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.find(nums, 0, len(nums)-1)
    
    def find(self, nums, low, high):
        if high-low <= 1:
            return min(nums)
        
        mid = (high+low)//2
        if mid < high:
            return min(nums[mid], self.find(nums, low, mid-1))
        else:
            return min(nums[low], self.find(nums, mid+1, high))
