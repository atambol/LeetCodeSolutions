class Solution:
    def __init__(self):
        self.parent = {}
        self.child = {}
        
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        # Disjoint set data structure
        for edge in edges:
            for v in edge:
                if v not in self.parent:
                    self.makeset(v)
                    
        for u, v in edges:
            parent_u = self.findset(u)
            parent_v = self.findset(v)
            
            if parent_u == parent_v:
                return [u, v]
            else:
                self.union(u, v)
        
    def makeset(self, v):    
        self.parent[v] = v
        self.child[v] = set([v])
        
    def findset(self, v):
        return self.parent[v]
    
    def union(self, u, v):
        parent_u = self.findset(u)
        parent_v = self.findset(v)
        
        if len(self.child[parent_u]) > len(self.child[parent_v]):
            self.updateParent(self.child[parent_v], parent_u)
            self.child.pop(parent_v)
        else:
            self.updateParent(self.child[parent_u], parent_v)
            self.child.pop(parent_u)
            
    def updateParent(self, children, parent):
        for child in children:
            self.parent[child] = parent
            self.child[parent].add(child)
