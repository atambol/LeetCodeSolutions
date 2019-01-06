class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # edge cases
        if not m or not n:
            return 0
        
        if m == 1 or n == 1:
            return 1
        
        # create a dp matrix
        dp = []
        for i in range(m):
            dp.append([0]*n)
        
        # one way to reach the first cell
        dp[0][0] = 1
        
        # find ways for other cells
        for i in range(m):
            for j in range(n):
                up = 0
                if i - 1 >= 0:
                    up = dp[i-1][j]
                left = 0
                if j - 1 >= 0:
                    left = dp[i][j-1]
                    
                dp[i][j] = left + up + dp[i][j]
                
        return dp[-1][-1]
