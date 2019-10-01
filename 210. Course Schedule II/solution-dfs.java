class Solution {
    enum State {
        visited, visiting, unvisited;
    }
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // State array stores visited information
        State[] states = new State[numCourses];
        for (int i = 0; i < numCourses; i++) {
            states[i] = State.unvisited;
        }
        
        // create adjacency list
        List<Integer>[] adj = new List[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        
        for (int i = 0; i < prerequisites.length; i++) {
            adj[prerequisites[i][0]].add(prerequisites[i][1]);
        }
        
        // solution
        int[] order = new int[numCourses];
        
        // dfs on all
        int ptr = 0;
        for (int course = 0; course < numCourses; course++) {
            if (states[course] == State.visited) {
                continue;
            }
            ptr = dfs(numCourses, course, adj, order, ptr, states);
            
            // cycle found, cannot take courses
            if (ptr == -1) {
                return new int[0];
            }
        }
        return order;
    }
    
    public int dfs(int numCourses, int course, List<Integer>[] adj, int[] order, int ptr, State[] states) {
        if (states[course] == State.visiting) {
            return -1;
        }
        
        states[course] = State.visiting;
        for (int prereq: adj[course]) {
            if (states[prereq] == State.visited) {
                continue;
            }
            else {
                ptr = dfs(numCourses, prereq, adj, order, ptr, states);
                if (ptr == -1) {
                    return -1;
                }
            }
        }
        
        order[ptr] = course;
        states[course] = State.visited;
        ptr++;
        return ptr; 
    } 
}
