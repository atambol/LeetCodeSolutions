class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        for pos, num in enumerate(nums):
            if target - num in complement:
                return [complement[target - num], pos]
            else:
                complement[num] = pos
