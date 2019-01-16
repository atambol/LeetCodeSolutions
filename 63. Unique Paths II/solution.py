class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # edge cases
        if not m or not n:
            return 0
        
        # start position is blocked
        if obstacleGrid[0][0] == 1:
            return 0
        
        # fill all the cells
        for i in range(m):
            dp.append([0]*n)
            
        # mark the first one with 1
        dp[0][0] = 1
        
        # fill the first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1
        
        # fill the first row
        for i in range(n):
            if obstacleGrid[0][i] == 0 and dp[0][i-1] == 1:
                dp[0][i] = 1

        # calculate the number of ways based on top and left values in dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]
