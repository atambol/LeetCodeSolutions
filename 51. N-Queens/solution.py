class Solution:
    def __init__(self):
        self.sol = []
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        config = []
        self.backtrack(n, config)
        return self.sol
    
    def backtrack(self, n, config):
        if len(config) == n:
            self.saveConfig(n, config)
        else:
            for i in range(n):
                isSafe = self.checkSafe(config, i)
                if isSafe:
                    config.append(i)
                    self.backtrack(n, config)
                    config.pop()
                    
    def checkSafe(self, config, y):
        x = len(config)
        for i in range(len(config)):
            if i == x or y == config[i]:
                return False
            if abs(i-x) == abs(config[i]-y):
                return False
        
        return True    
    
    def saveConfig(self, n, config):
        sol = []
        for i in range(n):
            sol.append(["."]*n)
            
        for i in range(len(config)):
            sol[i][config[i]] = "Q"
            
        sol2 = []
        for i in range(n):
            sol2.append("".join(sol[i]))
            
        self.sol.append(sol2)
        
