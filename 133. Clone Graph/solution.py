# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.graph = {}
    
    def cloneGraph(self, node):
        if not node:
            return None
        
        if node in self.graph:
            return self.graph[node]
        
        clone = UndirectedGraphNode(node.label)
        self.graph[node] = clone
        
        for neigh in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neigh))
            
        return clone
            
