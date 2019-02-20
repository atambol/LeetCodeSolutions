class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        # edge case
        if not nums:
            return 1
        
        # replace non-positive numbers with +infinity
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = sys.maxsize
        
        # for any number less than n, add a -ve sign to n-1th position
        for i in range(n):
            pos = abs(nums[i]) - 1
            if pos < n:
                nums[pos] = - abs(nums[pos])

        # check for a positive number at index i, and i + 1 is the solution
        for i in range(n):
            if nums[i] > 0:
                return i + 1
            
        # n + 1 is the solution if no number is found
        return n + 1
