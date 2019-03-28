class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol = []
        if not nums:
            return sol
        
        base = 0
        i = 0
        while i < len(nums):
            if nums[base] + i - base == nums[i]:
                i += 1
            else:
                if i - 1 == base:
                    sol.append(str(nums[base]))
                else:
                    sol.append(str(nums[base]) + "->" + str(nums[i-1]))
                base = i
                
        if i - 1 == base:
            sol.append(str(nums[base]))
        else:
            sol.append(str(nums[base]) + "->" + str(nums[i-1]))
            
        return sol
                
