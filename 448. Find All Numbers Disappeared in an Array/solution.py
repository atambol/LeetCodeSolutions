class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        res = []
        nums = set(nums)
        for i in range(1, l + 1):
            if i not in nums:
                res.append(i)
        return res
