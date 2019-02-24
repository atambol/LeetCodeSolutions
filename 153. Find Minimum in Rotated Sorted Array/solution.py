class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.myFindMin(nums, 0, len(nums)-1)
        
    def myFindMin(self, nums, i, j):
        if j-i <= 1:
            return min(nums[i:j+1])
        else:
            mid = (i+j)//2
            if nums[mid] < nums[j]:
                return min(nums[mid], self.myFindMin(nums, i, mid-1))
            else:
                return min(nums[i], self.myFindMin(nums, mid+1, j))
