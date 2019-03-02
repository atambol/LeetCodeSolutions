class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # edge case
        if not nums:
            return []
        
        # backtrack
        nums.sort()
        return self.backtrack(nums)
    
    def backtrack(self, nums):
        sol = []
        
        # base case
        if len(nums) == 1:
            sol.append([nums[0]])

        # backtrack more
        else:
            for i in range(len(nums)):
                # check for repetition
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                    
                sub = self.backtrack(nums[:i]+nums[i+1:])
                for s in sub:
                    s.append(nums[i])
                    sol.append(s)

        return sol
