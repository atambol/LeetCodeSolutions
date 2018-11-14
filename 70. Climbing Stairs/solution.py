class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev1 = 1
        prev2 = 2
        if n == 1:
            return prev1
        
        if n == 2:
            return prev2
            
        for i in range(3, n+1):
            tmp = prev1 + prev2
            prev1 = prev2
            prev2 = tmp
            
        return prev2
            
        
