# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def __init__(self):
        self.visited = {}
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # edge case
        if not node:
            return None
        
        # add to visited
        clone = UndirectedGraphNode(node.label)
        self.visited[node] = clone
        
        # get the neighbors
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                clone.neighbors.append(self.visited[neighbor])
            else:
                clone.neighbors.append(self.cloneGraph(neighbor))
                
        return clone
