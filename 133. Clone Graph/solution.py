# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        # initialize a visited dictionary
        self.visited = {}
    
    def cloneGraph(self, node):
        # edge case
        if not node:
            return node
        
        # if node was already visited, just return its clone
        if node in self.visited:
            return self.visited[node]
        else:
            # otherwise create a clone
            clone = UndirectedGraphNode(node.label)
            self.visited[node] = clone
            
            # visit node's neighbors
            for neigh in node.neighbors:
                clone.neighbors.append(self.cloneGraph(neigh))
                
            # return the clone
            return clone
