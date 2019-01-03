class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = self.createGraph(edges, n)
        start_vertices = list(graph)
        visited = set()
        
        # perform dfs from one vertex
        cycle = self.dfs(start_vertices[0], graph, visited)
        
        # no cycle should be present
        if cycle:
            return False
        
        # all vertices should have been visited (no forest allowed)
        for vertex in range(n):
            if vertex not in visited:
                return False
            
        return True
        
    def dfs(self, vertex, graph, visited):
        # catch cycle
        if vertex in visited:
            return True
        
        # mark visited
        visited.add(vertex)
        cycle = False
        
        # visit neighbours
        for neigh in graph[vertex]:
            # prevent it from coming back
            graph[neigh].remove(vertex)
            # dfs on neighbour
            cycle = self.dfs(neigh, graph, visited)
            if cycle:
                return cycle
        return cycle
        
    # create a graph from the edges
    def createGraph(self, edges, n):
        graph = {}
        for v in range(n):
            graph[v] = set()
            
        for e in edges:
            a = e[0]
            b = e[1]
            graph[a].add(b)
            graph[b].add(a)
            
        return graph
