class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        if not nums:
            return sol
        
        nums.sort()
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    sol.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                                        
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    while j < k and k+1 < len(nums) and nums[k] == nums[k+1]:
                        k -= 1
                        
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return sol
                    
