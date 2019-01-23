class Solution(object):
    def __init__(self):
        self.graph = {}
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # create a graph representation
        for x, y in equations:
            self.graph[x] = {x:1.0}
            self.graph[y] = {y:1.0}
            
        for i in range(len(equations)):
            x = equations[i][0]
            y = equations[i][1]
            self.graph[x][y] = values[i]
            self.graph[y][x] = 1/values[i]
            
        # perform dfs for each query
        sol = []
        for x, y in queries:
            if not x in self.graph or not y in self.graph:
                sol.append(-1.0)
            else:
                visited = set()
                tmp = self.dfs(visited, x, y)
                if tmp == None:
                    sol.append(-1.0)
                else:
                    sol.append(tmp)
        return sol
    
    def dfs(self, visited, x, y):
        visited.add(x)
        if y in self.graph[x]:
            return self.graph[x][y]
        
        for z in self.graph[x]:
            if not z in visited:
                sol = self.dfs(visited, z, y)
                if sol != None:
                    self.graph[x][y] = sol*self.graph[x][z]
                    return self.graph[x][y]
                
        return None
