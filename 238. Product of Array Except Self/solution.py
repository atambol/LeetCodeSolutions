class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        prod = 1
        for i in range(len(nums)):
            left[i] = prod
            prod *= nums[i]
            
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            left[i] = left[i]*prod
            prod *= nums[i]
            
        return left
