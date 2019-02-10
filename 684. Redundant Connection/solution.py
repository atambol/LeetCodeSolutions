class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # count the number of vertices
        # essentially implemented using disjoint set data structure
        # create the representative and components map
        rep = {}
        comp = {}
        for v, w in edges:
            if v not in rep:
                rep[v] = v
                comp[v] = set([v])
            if w not in rep:
                rep[w] = w
                comp[w] = set([w])
        
        # find the edge where both vertices have same representative element
        for edge in edges:
            v, w = edge[0], edge[1]
            if v in rep and w in rep and rep[v] == rep[w]:
                return edge
            else:
                rep_v = rep[v]
                rep_w = rep[w]
                if rep_v < rep_w:
                    rep[v] = rep_w
                    for c in comp[rep_v]:
                        comp[rep_w].add(c)
                        rep[c] = rep_w
                    comp.pop(rep_v)
                else:
                    rep[w] = rep_v
                    for c in comp[rep_w]:
                        comp[rep_v].add(c)
                        rep[c] = rep_v
                    comp.pop(rep_w)
                    
            
