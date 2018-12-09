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
        self.makeGraph(equations, values)
        sol = []
        for query in queries:
            a = query[0]
            b = query[1]
            
            # if either variables are not in graph, return -1.0
            if a not in self.graph or b not in self.graph:
                sol.append(-1.0)
            # a/a = 1.0
            elif a == b:
                sol.append(1.0)
            # perform dfs
            else:
                visited = set()
                sol.append(self.dfs(a, b, visited))
        return sol
    
    # construct a graph with vertices as variables and edges as values        
    def makeGraph(self, equations, values):
        for eq, val in zip(equations, values):
            a = eq[0]
            b = eq[1]
            if not a in self.graph:
                self.graph[a] = {}
            self.graph[a][b] = val
            if not b in self.graph:
                self.graph[b] = {}
            self.graph[b][a] = 1/val
    
    # dfs over graph for a,b
    def dfs(self, a, b, visited):
        if b in self.graph[a]:
            return self.graph[a][b]
        
        visited.add(a)
        for v in self.graph[a].keys():
            if not v in visited:
                val = self.dfs(v, b, visited)
                if val != -1.0:
                    return val * self.graph[a][v]
        return -1.0
        
