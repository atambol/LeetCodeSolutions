class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        config = set()
        self.sol = []
        self.backtrack(config, n)
        return self.sol
        
    def backtrack(self, config, n):
        if len(config) == n:
            self.saveState(config)
        else:
            i = len(config)
            for j in range(n):
                if self.safeState(config, i, j):
                    config.add((i,j))
                    self.backtrack(config, n)
                    config.remove((i, j))
                    
    def safeState(self, config, i, j):
        for x, y in config:
            if abs(x-i) == abs(y-j) or x == i or y == j:
                return False
            
        return True
    
    def saveState(self, config):
        sol = []
        for i in range(len(config)):
            s = []
            for j in range(len(config)):
                if (i, j) in config:
                    s.append("Q")
                else:
                    s.append(".")
                    
            sol.append("".join(s))
        self.sol.append(sol)
