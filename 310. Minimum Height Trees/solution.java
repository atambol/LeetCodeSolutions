class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (edges.length == 0) {
            List<Integer> sol = new ArrayList<Integer>();
            sol.add(0);
            return sol;
        }
        
        // create graph
        HashSet<Integer> adj;
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>();
        for (int[] edge: edges) {
            if (!graph.containsKey(edge[0])) {
                adj = new HashSet<Integer>();
                graph.put(edge[0], adj);
            } else {
                adj = graph.get(edge[0]);
            }
            adj.add(edge[1]);
            
            if (!graph.containsKey(edge[1])) {
                adj = new HashSet<Integer>();
                graph.put(edge[1], adj);
            } else {
                adj = graph.get(edge[1]);
            }
            adj.add(edge[0]);   
        }
        
        // get all the vertices with one edge 
        List<Integer> oneEdged = new ArrayList<>();
        int i = 0;
        for (Map.Entry<Integer,HashSet<Integer>> entry : graph.entrySet()) {
            if (entry.getValue().size() == 1) {
                oneEdged.add(entry.getKey());
            }
        }
        List<Integer> aux = new ArrayList<>();
        List<Integer> tmp;
        while (!oneEdged.isEmpty()) {
            for (Integer vertex: oneEdged) {
                for (Integer neigh: graph.get(vertex)) {
                    adj = graph.get(neigh);
                    adj.remove(vertex);
                    if (adj.size() == 1) {
                        aux.add(neigh);
                    }
                }
                graph.remove(vertex);
            }
            
            if (aux.isEmpty()) {
                break;
            } else {
                tmp = aux;
                aux = oneEdged;
                oneEdged = tmp;
                aux.clear();
            }
        }
        
        return oneEdged;
    }
}
