class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.myFindMin(nums, 0, len(nums)-1)
        
    def myFindMin(self, nums, low, high):
        if high - low == 1:
            return min(nums[low], nums[high])
        elif high - low == 0:
            return nums[low]
        
        mid = (low+high)//2
        
        # if mid element is not giving clear indications, O(n)
        if nums[mid] == nums[high] or nums[mid] == nums[low]:
            return min(self.myFindMin(nums, low, mid-1), self.myFindMin(nums, mid, high))
        # look on one side only O(logn)
        if nums[mid] < nums[high]:
            return min(self.myFindMin(nums, low, mid-1), nums[mid])
        else:
            return min(self.myFindMin(nums, mid+1, high), nums[low])
        
