class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # edge cases
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        if not n:
            return 0
        
        # dp
        dp = []
        for i in range(m):
            dp.append([0]*n)
            
        area = 0
        
        # fill first row and column
        for i in range(n):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                area = 1
                
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                area = 1
                
        # fill the rest
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    area = max(area, dp[i][j])
        
        return area**2
