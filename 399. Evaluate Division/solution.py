class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        nil = -1.0
        
        # create a graphical representation of equations
        graph = {}
        for e, v in zip(equations, values):
            x = e[0]
            y = e[1]
            if not x in graph:
                graph[x] = {}
                
            if not y in graph:
                graph[y] = {}
                
            graph[x][y] = v
            graph[y][x] = 1/v
            
            graph[x][x] = 1.0
            graph[y][y] = 1.0
            
        # dfs
        def dfs(graph, a, b, visited):
            if b in graph[a]:
                return graph[a][b]
            if a in visited:
                return nil
            visited.add(a)
            for c in graph[a]:
                ans = dfs(graph, c, b, visited)
                if ans != nil:
                    ans *= graph[a][c]
                    graph[a][b] = ans
                    return ans
            return nil
        
        # solve the queries
        sol = []
        for x, y in queries:
            visited = set()
            if x not in graph or y not in graph:
                sol.append(nil)
            else:
                sol.append(dfs(graph, x, y, visited))
            
        return sol
