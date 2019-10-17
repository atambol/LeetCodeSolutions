class Solution {
    private int unvisited = 0;
    private int visiting = 1;
    private int visited = 2;
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> graph = new HashMap<Integer, List<Integer>>();
        
        // create adj list
        List<Integer> adj;
        for (int i = 0; i < numCourses; i++) {
            adj = new ArrayList<Integer>();
            graph.put(i, adj);
        }
        
        // fill the list
        for (int i = 0; i < prerequisites.length; i++) {
            adj = graph.get(prerequisites[i][0]);
            adj.add(prerequisites[i][1]);
        }
        
        // check for cycle
        int[] status = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (status[i] == unvisited)
                if (hasCycle(graph, i, status))
                    return false;
        }
        
        return true;
    }
    
    public boolean hasCycle(HashMap<Integer, List<Integer>> graph, int course, int[] status) {
        status[course] = visiting;
        List<Integer> adj = graph.get(course);
        for (Integer neigh: adj) {
            if (status[neigh] == visited)
                continue;
            if (status[neigh] == visiting) 
                return true;
            if (hasCycle(graph, neigh, status)) {
                return true;
            }
        }
        status[course] = visited;
        return false;
    }
}
