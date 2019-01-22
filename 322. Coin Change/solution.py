class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # edge cases
        if not coins:
            return -1
        
        if not amount:
            return 0
        
        if amount < 0:
            return -1
        
        minDeno = min(coins)
        if minDeno > amount:
            return -1
        
        # dynamic programming
        dp = [-1]*(minDeno)
        dp[0] = 0
        
        for i in range(minDeno, amount+1):
            change = sys.maxsize
            for c in coins:
                if i - c == 0:
                    change = 1
                    break
                else:
                    if i -c >= 0 and dp[i-c] > 0:
                        change = min(change, dp[i-c] + 1)
                    
            if change == sys.maxsize:
                dp.append(-1)
            else:
                dp.append(change)
                
        return dp[-1]
        
