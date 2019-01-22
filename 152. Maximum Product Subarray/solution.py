class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = nums[0]
        pos = nums[0]
        prod = nums[0]
        for num in nums[1:]:
            candidates = [neg*num, pos*num, num]
            neg = min(candidates)
            pos = max(candidates)
            prod = max(pos, prod)
            
        return prod
