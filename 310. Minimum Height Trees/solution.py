class Solution:
    def __init__(self):
        self.graph = {}
        
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # edge cases
        if n == 1:
            return [0]
        
        # construct the bidirectional graph
        for v in range(n):
            self.graph[v] = set()
            
        for e1, e2 in edges:
            self.graph[e1].add(e2)
            self.graph[e2].add(e1)

        leaves = set([v for v in self.graph if len(self.graph[v]) == 1])
        
        # start from leaves and move inwards        
        # remove leaves, break edges and recalculate leaves
        # since it is a tree, the final solution will contain up to 2 nodes
        while n > 2:
            n -= len(leaves)
            
            # store all the leaves here
            newleaves = set()
            for node in leaves:
                # for each neighbour break the edge
                # recalculate leaf status
                for neigh in self.graph[node]:
                    self.graph[neigh].remove(node)
                    if len(self.graph[neigh]) == 1:
                        newleaves.add(neigh)
            leaves = newleaves
            
        return list(leaves)
