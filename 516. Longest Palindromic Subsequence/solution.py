class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge cases
        n = len(s)
        if not s:
            return 0
        
        # dynamic programming
        dp = []
        for i in range(n):
            dp.append([0]*n)
            
        for i in range(n-1, -1, -1):
            # palindrome around itself
            dp[i][i] = 1
            
            # look at all the substring from i + 1 -> n
            for j in range(i+1, n):
                # if same chars then look at the first cell anti diagonally
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                # if not, it is the maximum of what is seen so far to the left and below
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][-1]
