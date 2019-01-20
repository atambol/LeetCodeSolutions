class Solution:
    def __init__(self):
        self.sol = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        config = set()
        self.backtrack(n, 0, config)
        return self.sol
        
    def backtrack(self, n, i, config):
        if i == n:
            self.saveSol(n, config)
            
        for j in range(n):
            if self.isSafe(i, j, config):
                config.add((i, j))
                self.backtrack(n, i+1, config)
                config.remove((i, j))
                    
    def isSafe(self, i, j, config):
        for x, y in config:
            if i == x or j == y or (abs(i-x) == abs(j-y)):
                return False
            
        return True
    
    def saveSol(self, n, config):
        sol = []
        for i in range(n):
            sol.append(["."]*n)
            
        for x, y in config:
            sol[x][y] = "Q"
            
        strSol = ["".join(s) for s in sol]
        self.sol.append(strSol)
