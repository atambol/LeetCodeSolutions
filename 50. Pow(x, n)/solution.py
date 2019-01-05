class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # edge cases
        if n == 0:
            return 1
        if n < 0 and x == 0:
            return None
        if x == 0:
            return 0
        
        # if negative power
        neg = n < 0
        n = abs(n)
        
        # calculate the powers 
        dp = x
        pw = 1
        
        while n:
            m = (n>>1)<< 1
            if m != n:
                pw *= dp
            dp = dp*dp
            n = n >> 1
        
        if not neg:
            return pw
        else:
            return 1/pw
