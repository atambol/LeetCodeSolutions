class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        
        # create the l*l array to store intermediate solutions
        dp = {}
        for i in range(l):
            dp[i] = {}
        
        # run through each numbers in reverse order
        # use dp to calculate the products
        # count the number of products less than k
        count = 0
        for i in range(l-1, -1, -1):
            dp[i][i] = nums[i]
            if nums[i] < k:
                count += 1
                for j in range(i+1, l, 1):
                    dp[i][j] = dp[i][j-1] * nums[j]
                    if dp[i][j] < k:
                        count += 1
                    else:
                        break
                    
        return count
