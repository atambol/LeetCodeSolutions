class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # edge cases
        if not amount:
            return 0
        
        if not coins or amount < 0 or amount < min(coins):
            return -1
        
        # dp
        change = [0]*(amount+1)
        coins.sort()
        
        for i in range(1, amount+1):
            minChange = sys.maxsize
            for coin in coins:
                if i - coin < 0:
                    continue
                elif i - coin == 0:
                    minChange = 1
                else:
                    if change[i-coin] != -1:
                        minChange = min(1 + change[i-coin], minChange)
                        
            if minChange == sys.maxsize:
                minChange = -1
            change[i] = minChange
            
        return change[-1]
