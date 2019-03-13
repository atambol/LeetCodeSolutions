class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if not s:
            return 0
        
        # prepare for dp
        dp = []
        n = len(s)
        for i in range(n):
            dp.append([0]*n)
            
        # check for palindromic subsequences
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][-1]
