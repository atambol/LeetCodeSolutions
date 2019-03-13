class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # prepare for dp
        word1 = "#" + word1
        word2 = "#" + word2
        m = len(word1)
        n = len(word2)
        dp = []
        for i in range(m):
            dp.append([0]*n)
            
        for i in range(m):
            dp[i][0] = i
        for i in range(n):
            dp[0][i] = i
            
        # dp
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
        return dp[-1][-1]
