class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # this solution uses DFS to traverse all possible scenarios
        # this is brute force and times out on the last case
        
        # edge case
        if len(prices) <= 1:
            return 0
        
        # total profits for index i
        profits = [0]*len(prices)
        
        # if index i is visited or not
        visited = [0]*len(prices)
        
        # initiate the dfs for first 3 indices
        for i in range(3):
            self.dfs(prices, i, profits, visited)
        
        return max(profits)
    
    def dfs(self, prices, start, profits, visited):
        # check if start is beyond the length of prices
        if start >= len(prices):
            return 0
        
        # if already visited, return memoised result
        if visited[start]:
            return profits[start]
        
        # calculate profit by going over each possible iteration to maximise total profit
        totalProfit = profits[start]
        profit = 0
        for end in range(start+1, len(prices)):
            profit = max(profit, prices[end] - prices[start])
            nextProfit = self.dfs(prices, end + 2, profits, visited)
            totalProfit = max(totalProfit, profit + nextProfit)
        
        # memoise results
        profits[start] = totalProfit
        
        # mark visited
        visited[start] = 1
        
        return totalProfit
