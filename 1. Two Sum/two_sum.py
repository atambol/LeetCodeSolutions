class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numtab = {}
        for i, num1 in enumerate(nums):
            try:
                num2 = target - num1
                if numtab[num2] >= 0:
                    return [numtab[num2], i]
            except KeyError as e:
                numtab[num1] = i

            
        return []
