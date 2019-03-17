## Linked List
* Add a dummy head node to the front to avoid explicitly handling edge cases
* Fast pointer and slow pointer technique
* Check for empty list

## Trees
* Iterative 
* Recursive 
* Check for empty tree node
* 4 case technique for binary tree children

## Strings
* Check case sensitivity
* Check encoding

## Arrays
* Two pointer technique
* DFS

## Dynamic programming
* Tabulate the previous results and construct new results using them

## Graphs
* DFS
* BFS
* Disjoint set datastructure - useful for checking connected components, finding cycles in undirected graph etc
```python
# Using 2 optimisations - path compression and union by rank
# Amortized time complexity per operation is O(alpha(n)) which is near constant
class DSD:
    def __init__(self):
        self.parents = {}
        self.children = {}
        
    def makeset(self, node): 
        # O(1) time complexity
        self.parents[node] = node
        self.children[node] = set([node])
        
    def find(self, node):
        # O(1) time complexity
        return self.parents[node]
    
    def union(self, node1, node2):
        # O(logn) time complexity
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        # implies no union (cycle)
        if parent1 == parent2:
            return False
        
        # adopt children of parent with least number of children
        # optimisation 1 = union by rank
        if len(self.children[parent1]) < len(self.children[parent2]):
            self.update(parent1, parent2)
        else:
            self.update(parent2, parent1)
        
        # union successful
        return True
    
    def update(self, oldparent, newparent):
        # optimisation 2 = path compression
        # new parent adopts children of old parent
        # children directly point to the new parent
        for child in self.children[oldparent]:
            self.parents[child] = newparent
            self.children[newparent].add(child)
            
        # old parent does not have any children anymore
        self.children[oldparent] = set()
        
        # new parent adopts old parent
        self.children[newparent].add(oldparent)
        self.parents[oldparent] = newparent
```
* Toplogical sort
  * modified DFS - maintain three states (unvisited, visiting and visited)
  * Kahn's algorithm - maintain in-degrees of vertices (BFS like)
* Complexity of BFS and DFS is O(V+E) for adjacency list and O(V^2) for adjacency matrix representation
