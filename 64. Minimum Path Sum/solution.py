class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = []
        m = len(grid)
        n = len(grid[0])
        if not m or not n:
            return 0
        
        for i in range(m):
            dp.append([0]*n)
        
        prev = 0 
        for i in range(m):
            dp[i][0] = prev + grid[i][0]
            prev = dp[i][0]
            
        prev = 0 
        for i in range(n):
            dp[0][i] = prev + grid[0][i]
            prev = dp[0][i]
             
        for i in range(1, m):
            for j in range(1, n):
                top = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = min(top, left) + grid[i][j]
                
        return dp[-1][-1]
                    
                
