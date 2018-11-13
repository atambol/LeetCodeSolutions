class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort and initialize seen set to not repeat the first element
        nums.sort()
        seen = set()
        
        # repeat contains string representations of previously added solutions
        repeat = set()
        
        # final solution
        sol = list()
        
        # Loop to get the first element
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                
            # Complement array stores previously seen elements in 2 sum
            complement = set()
            
            # begin 2sum
            for j in range(i+1, len(nums)):
                target = (nums[i] + nums[j]) * -1

                if target in complement:
                    key = "{},{},{}".format(nums[i], target, nums[j])
                    if key in repeat:
                        continue
                    else:
                        repeat.add(key)
                        sol.append([nums[i], target, nums[j]])
                    
                complement.add(nums[j])
                    
        return sol
                    
