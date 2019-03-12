class Solution:
    def __init__(self):
        self.graph = {}
        self.status = []
        self.unvisited = 0
        self.visiting = 1
        self.visited = 2
        
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        # create a graph
        for i in range(n):
            self.graph[i] = set()
            
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)
            
        # dfs over all edges and check for cycle
        self.status = [self.unvisited]*n
        cycle = self.dfs(0)
        if cycle:
            return False
        
        # check for forest
        return self.status.count(self.visited) == n

        
    def dfs(self, node):
        if self.status[node] == self.visiting:
            return True
        elif self.status[node] == self.visited:
            return False
        else:
            self.status[node] = self.visiting

        for neigh in self.graph[node]:
            self.graph[neigh].remove(node)
            cycle = self.dfs(neigh)
            if cycle:
                return True

        self.status[node] = self.visited
        return False
        
        
