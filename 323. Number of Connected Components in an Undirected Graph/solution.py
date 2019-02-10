class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # create graph
        graph = {}
        for v in range(n):
            graph[v] = set()
        for v, w in edges:
            graph[v].add(w)
            graph[w].add(v)
                
        # perform dfs and count number of components
        count = 0
        visited = [False]*n
        for v in range(n):
            if not visited[v]:
                self.dfs(graph, visited, v)
                count += 1
                
        return count
    
    def dfs(self, graph, visited, v):
        if visited[v]:
            return
        visited[v] = True
        
        for w in graph[v]:
            self.dfs(graph, visited, w)
