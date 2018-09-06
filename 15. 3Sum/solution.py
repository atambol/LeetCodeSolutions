from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        added = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
        l = len(nums)
        if l < 3:
            return res
        
        nums.sort()
        repeat_count = defaultdict(lambda: 0)
        for i in range(0, l-2):
            if repeat_count[nums[i]] >= 3:
                continue
            else:
                repeat_count[nums[i]] += 1

            sum = 0 - nums[i]
            seen = set()

            for j in range(i+1, l):
                complement = sum - nums[j]
                if complement in seen:
                    if not added[nums[i]][complement][nums[j]]:
                        res.append([nums[i], complement, nums[j]])
                        added[nums[i]][complement][nums[j]] = True
                seen.add(nums[j])

        return res
