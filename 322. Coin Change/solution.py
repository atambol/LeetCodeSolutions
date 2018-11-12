class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        
        noSolution = -1
        firstDenomination = min(coins)
        coinCountMax = amount + 1
        if amount < firstDenomination:
            return noSolution
        
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for amt in range(firstDenomination, amount + 1):
            count = coinCountMax
            for coin in coins:
                prev = amt - coin
                if prev >= 0 and dp[prev] != -1 and dp[prev] + 1 < count:
                    count = dp[prev] + 1
                
            if count != coinCountMax:
                dp[amt] = count
            else:
                dp[amt] = noSolution
                    
        return dp[amt]
