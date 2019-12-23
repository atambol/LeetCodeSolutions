class Solution {
    private int visited = 2;
    private int visiting = 1;
    private int unvisited = 0;
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = getGraph(numCourses, prerequisites);
        int[] visitStatus = new int[numCourses];
        List<Integer> topSort = new ArrayList<Integer>();
        int[] topSortArray = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (dfs(i, graph, visitStatus, topSort) == false) {
                return new int[0];
            }
        }
        
        int i = 0;
        for (int course: topSort) {
            topSortArray[i++] = course;
        }
        return topSortArray;
    }
    
    public boolean dfs(int course, 
                    Map<Integer, List<Integer>> graph, 
                    int[] visitStatus,
                    List<Integer> topSort) {
        if (visitStatus[course] == visiting) {
            return false;
        }
        if (visitStatus[course] == visited) {
            return true;
        }
        visitStatus[course] = visiting;
        List<Integer> adjList = graph.get(course);
        for (Integer prereq: adjList) {
            if (dfs(prereq, graph, visitStatus, topSort) == false) {
                return false;
            }
        }
        visitStatus[course] = visited;
        topSort.add(course);
        return true;
    }
    
    public Map<Integer, List<Integer>> getGraph(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<Integer>());
        }
        
        List<Integer> adjList;
        for (int[] edge: prerequisites) {
            adjList = graph.get(edge[0]);
            adjList.add(edge[1]);
        }
        return graph;
    }
}
