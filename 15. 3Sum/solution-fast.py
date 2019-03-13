class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        
        # edge case
        if not nums:
            return sol
        
        # sort the nums
        nums.sort()
        
        # loop over each one
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i and nums[i] == nums[i-1]:
                continue
                
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    sol.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
                elif target > 0:
                    k -= 1
                else:
                    j += 1
                    
        return sol
                    
