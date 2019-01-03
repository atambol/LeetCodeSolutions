class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # sum left
        suml = []
        total = 0
        for i in range(n):
            total += nums[i]
            suml.append(total)
            
        # sum right
        sumr = []
        total = 0
        for i in range(n-1, -1, -1):
            total += nums[i]
            sumr.append(total)
        sumr.reverse()
        
        # check equality
        for i in range(n):
            if sumr[i] == suml[i]:
                return i
            
        return -1
