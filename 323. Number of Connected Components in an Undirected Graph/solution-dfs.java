class Solution {
    public int countComponents(int n, int[][] edges) {
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>();
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            graph.put(i, new HashSet<Integer>());
            visited[i] = false;
        }
        
        HashSet<Integer> adj;
        for (int[] edge: edges) {
            adj = graph.get(edge[0]);
            adj.add(edge[1]);
            adj = graph.get(edge[1]);
            adj.add(edge[0]);
        }
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited);
                count++;
            }
        }
        
        return count;
    }
    
    public void dfs(int vertex, HashMap<Integer, HashSet<Integer>> graph, boolean[] visited) {
        if (visited[vertex]) {
            return;
        }
        
        visited[vertex] = true;
        HashSet<Integer> adj = graph.get(vertex);
        for (int neigh: adj) {
            dfs(neigh, graph, visited);
        }
    }
}
