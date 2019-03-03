class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        
        # edge cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        # dp grid
        dp = []
        for i in range(l1+1):
            dp.append([0]*(l2+1))
            
        for i in range(l1+1):
            dp[i][0] = i
        
        for i in range(l2+1):
            dp[0][i] = i
            
        # insert a dummy character to the start
        word1 = "."+word1
        word2 = "."+word2
        
        # find the edit distance
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1) + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
        return dp[-1][-1]
