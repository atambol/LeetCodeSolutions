class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # edge cases
        sol = set()
        n = len(nums)
        if not n:
            return []
        
        nums.sort()
        seen = set()
        
        # 3 sum
        for i in range(n):
            if nums[i] in seen:
                continue
            
            seen.add(nums[i])
            target = - nums[i]
            # 2 sum
            complement = set()
            for j in range(i+1, n):
                if target - nums[j] in complement:
                    sol.add((nums[i], target - nums[j], nums[j]))
                complement.add(nums[j])
                
        return list(sol)
                
        
