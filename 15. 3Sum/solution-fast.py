class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sol = []
        n = len(nums)
        for i in range(n-2):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    sol.append([nums[i], nums[j], nums[k]])
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    k -= 1
                    j += 1
                    
        return sol
