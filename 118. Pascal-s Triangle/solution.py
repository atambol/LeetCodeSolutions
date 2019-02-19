class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        sol = []
        if numRows == 0:
            return sol
        sol.append([1])
        if numRows == 1:
            return sol
        sol.append([1,1])
        if numRows == 2:
            return sol
        
        for i in range(3, numRows+1):
            s = [sol[-1][0]]
            for j in range(1, len(sol[-1])):
            s.append(sol[-1][-1])
            sol.append(s)
            
        return sol
            
