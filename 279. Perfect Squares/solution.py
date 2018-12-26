class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [0]
        s = 1
        dp = [0]
        
        for i in range(1, n+1):
            if s*s <= i:
                squares.append(s*s)
                s += 1
                
            count = sys.maxsize
            for j in squares[1:]:
                count = min(count, dp[i-j] + 1)
            dp.append(count)
            
        return dp[n]
