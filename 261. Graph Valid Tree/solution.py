class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = None
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # create a graph representation
        for i in range(n):
            self.graph[i] = set()
            
        for x, y in edges:
            self.graph[x].add(y)
            self.graph[y].add(x)
            
        # create a visited set
        self.visited = [False]*n
        
        # perform dfs from one node
        isCycle = self.dfs(0, None)
        
        # check for cycle
        if isCycle:
            return False
        
        # check for forest
        if self.visited.count(True) == n:
            return True
        else:
            return False
        
    def dfs(self, node, parent):
        self.visited[node] = True
        for neigh in self.graph[node]:
            if neigh != parent:
                if self.visited[neigh]:
                    return True
                else:
                    self.dfs(neigh, node)
                    
        return False
