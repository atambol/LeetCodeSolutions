class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # edge case
        if n <= 1:
            return True
            
        if not edges:
            return False
        
        # create a graph
        graph = {}
        for v in range(n):
            graph[v] = set()
            
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            
        # dfs
        def dfs(visited, v):  
            if visited[v] == 1:
                return False
            
            # mark visited
            visited[v] = 1
            
            for neigh in graph[v]:
                # prevent cycling back to the parent
                graph[neigh].remove(v)
                
                # visit children
                if not dfs(visited, neigh):
                    return False

            return True
        
        # start from one vertex and dfs should visit all of them
        visited = [0]*n
        start = edges[0][0]
        if not dfs(visited, start):
            # cycle detected
            return False
        
        if sum(visited) != n:
            # forest detected
            return False
        
        return True
        
            
