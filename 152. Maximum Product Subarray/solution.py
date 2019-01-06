class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = [nums[0]]
        pos = [nums[0]]
        
        for num in nums[1:]:
            options = [num, num*neg[-1], num*pos[-1]]
            neg.append(min(options))
            pos.append(max(options))
            
        return max(pos+neg)
