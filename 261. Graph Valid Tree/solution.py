class Solution(object):
    def __init__(self):
        self.graph = {}
        self.visited = set()
        self.unvisited = None

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # construct a graph from the given list
        self.createGraph(n, edges)
        
        # maintain an unvisited set - this catches the case when edges form a forest
        self.unvisited = set(range(n))
        
        # parent and child node for initial iteration
        parent = None
        node = 0
        
        # perform dfs
        allVisited = self.dfs(node, parent)
        
        # all nodes should be visited exactly once
        return allVisited and len(self.unvisited) == 0

    # create an undirected graph in the form of a dictionary
    def createGraph(self, n, edges):
        for i in range(n):
            self.graph[i] = set()
            
        for edge in edges:
            a = edge[0]
            b = edge[1]
            
            self.graph[a].add(b)
            self.graph[b].add(a)
        
    # dfs from node
    def dfs(self, node, parent):
        # if the node is already visited, there is a cycle
        if node in self.visited:
            print(node, parent, False)
            return False
        
        self.visited.add(node)
        self.unvisited.remove(node)
        allVisited = True

        # visit every neighbour other than the parent
        for neighbour in self.graph[node]:
            if neighbour != parent:
                allVisited = allVisited and self.dfs(neighbour, node)
            
        return allVisited
