class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = -sys.maxsize - 1
        maxtotal = -sys.maxsize - 1
        for num in nums:
            total = max(num, num + total)
            maxtotal = max(total, maxtotal)
            
        return maxtotal
