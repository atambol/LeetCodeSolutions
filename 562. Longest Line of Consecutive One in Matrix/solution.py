class Vals:
    def __init__(self, val):
        self.up = val
        self.left = val
        self.diag = val
        self.anti = val
    
class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        maxOne = 0
        dp = []
        width = len(M[0]) - 1
        
        # Dynamic programming to store results of previously visited indices
        for i in range(len(M)):
            dp.append([])
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    dp[i].append(Vals(1))
                else:
                    dp[i].append(Vals(0))

        # Visit M[i][j] and calculate the values
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    if i - 1 >= 0:
                        # Check up
                        dp[i][j].up = dp[i-1][j].up + 1

                        # Check anti
                        if j + 1 <= width:
                            dp[i][j].anti = dp[i-1][j+1].anti + 1

                        # Check diag
                        if j - 1 >= 0:
                            dp[i][j].diag = dp[i-1][j-1].diag + 1

                    # Check left
                    if j - 1 >= 0:
                        dp[i][j].left = dp[i][j-1].left + 1
                
                # Is this the largest value seen so far?
                maxCellOne = max(dp[i][j].up, dp[i][j].anti, dp[i][j].diag, dp[i][j].left)
                if maxCellOne > maxOne:
                    maxOne = maxCellOne
                    
        # for i in range(len(M)):
        #     for j in range(len(M[i])):
        #         print([i,j], dp[i][j].anti, dp[i][j].up, dp[i][j].diag, dp[i][j].left)

        return maxOne
