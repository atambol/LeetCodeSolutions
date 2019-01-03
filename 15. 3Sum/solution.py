class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort the input
        nums.sort()
        
        # do not allow repeated solutions
        repeat = set()
        
        # add element once it is pointed to by i
        seen = set()
        
        # final sol
        sol = []
        
        n = len(nums)
        
        # loop over every index
        for i in range(n):
            # save time by not going over repeat elements
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                
            # begin 2sum
            complement = set()
            for j in range(i+1, n):
                target = -nums[i] -nums[j]
                if target in complement and (nums[i], target, nums[j]) not in repeat:
                        sol.append([nums[i], target, nums[j]])
                        repeat.add((nums[i], target, nums[j]))
                complement.add(nums[j])
                    
            seen.add(nums[i])
                        
        return sol
        
