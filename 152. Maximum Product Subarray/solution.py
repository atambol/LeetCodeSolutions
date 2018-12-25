class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maintain two lists
        # pos contains the most positive product of subarray
        # neg contains the most negative product of subarray
        if nums[0] >= 0:
            pos = nums[0]
            neg = 0
        else:
            neg = nums[0]
            pos = 0
        
        # prod is our solution
        prod = nums[0]
        
        # iterate through each number
        for i, num in enumerate(nums[1:]):
            # get the most positive and negative product for this iteration
            pos, neg = max(neg*num, pos*num, num), min(neg*num, pos*num, num)
            
            # check if there is a more positive product
            prod = max(pos, prod)
        return prod
