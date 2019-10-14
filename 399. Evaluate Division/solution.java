class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // create graph
        Map<String, Map<String, Double>> graph = new HashMap<String, Map<String, Double>>();
        HashSet<String> vertices = new HashSet<String>();
        int n = values.length;
        List<String> equation;
        Map<String, Double> adjList;
        
        for (int i = 0; i < n; i++) {
            equation = equations.get(i);
            
            // update vertices
            vertices.add(equation.get(0));
            vertices.add(equation.get(1));
            
            // insert self
            if (!graph.containsKey(equation.get(0))) {
                adjList = new HashMap<String, Double>();
                adjList.put(equation.get(0), 1.0);
                graph.put(equation.get(0), adjList);
            }
            
            if (!graph.containsKey(equation.get(1))) {
                adjList = new HashMap<String, Double>();
                adjList.put(equation.get(1), 1.0);
                graph.put(equation.get(1), adjList);
            }
        }
        
        // update graph
        for (int i = 0; i < n; i++) {
            equation = equations.get(i);
            
            // insert edge
            adjList = graph.get(equation.get(0));
            adjList.put(equation.get(1), values[i]);
            
            // insert reverse edge
            adjList = graph.get(equation.get(1));
            adjList.put(equation.get(0), 1/values[i]);
        }
        
        // run through queries
        HashSet<String> visited = new HashSet<String>();
        double[] sol = new double[queries.size()];
        List<String> query = new ArrayList<String>();
        double value;
        for(int i = 0; i < queries.size(); i++) {
            query = queries.get(i);
            if (!vertices.contains(query.get(0)) || !vertices.contains(query.get(0))) {
                sol[i] = -1.0;
            } else {
                value = dfs(graph, visited, query.get(0), query.get(1));
                sol[i] = value;
            }
        }
        
        return sol;
    }
    
    public double dfs(Map<String, Map<String, Double>> graph, 
                      HashSet<String> visited, 
                      String start,
                      String end) {
        // edge case
        if (!graph.containsKey(start)) {
            return -1.0;
        }
        
        // get the adj list
        Map<String, Double> adjList = graph.get(start);
        if (adjList.containsKey(end)) {
            return adjList.get(end);
        }
        
        // check neighbouring vertices
        visited.add(start);
        double sol = -1.0;
        for (String neigh: adjList.keySet()) {
            if (visited.contains(neigh)) {
                continue;
            }
            
            sol = dfs(graph, visited, neigh, end);
            if (sol != -1) {
                sol *= adjList.get(neigh);
                
                // save solution
                adjList.put(end, sol);
                break;
            }
        }
        
        visited.remove(start);
        return sol;
    }
}
