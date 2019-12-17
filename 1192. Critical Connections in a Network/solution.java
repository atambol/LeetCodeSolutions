class Solution {
    public int unvisited = -1;
    public List<Integer>[] graph;
    public int[] visited;
    public List<List<Integer>> criticalEdges;
    
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        graph = getGraph(n, connections);
        visited = getVisitedArray(n);
        criticalEdges = new ArrayList<List<Integer>>();
        dfs(0, 0, -1);
        return criticalEdges;
    }
    
    public int dfs(int vertex, 
                   int rank,
                   int parent) {
        // mark visited
        visited[vertex] = rank;
        
        // dfs on neighbour
        int lowestRank = rank;
        int currentRank;
        for (int neigh: graph[vertex]) {
            if (parent == neigh)
                continue;
            if (visited[neigh] == unvisited) {
                currentRank = dfs(neigh, rank+1, vertex);
                if (currentRank <= rank) {
                    lowestRank = Math.min(currentRank, lowestRank);
                } else {
                    criticalEdges.add(getOrderedEdge(vertex, neigh));
                }
            } else {
                lowestRank = Math.min(visited[neigh], lowestRank);
            }
        }
        return lowestRank;
    }
    
    public int[] getVisitedArray(int n) {
        int[] visited = new int[n];
        for (int i = 0; i < n; i++)
            visited[i] = unvisited;
        
        return visited;
    }
    
    public List<Integer>[] getGraph(int n, List<List<Integer>> connections) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        
        int x, y;
        for (List<Integer> edge: connections) {
            x = edge.get(0);
            y = edge.get(1);
            graph[x].add(y);
            graph[y].add(x);
        }
        
        return graph;
    }
    
    public List<Integer> getOrderedEdge(int x, int y) {
        List<Integer> edge = new ArrayList<>(2);
        edge.add(x);
        edge.add(y);
        return edge;
    }
}
