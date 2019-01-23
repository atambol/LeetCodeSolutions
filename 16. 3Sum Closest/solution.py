class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sol = nums[0] + nums[1] + nums[2]
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > target:
                    k -= 1
                else:
                    j += 1
                
                if abs(sol-target) > abs(total-target):
                    sol = total
                    
        return sol
                    
