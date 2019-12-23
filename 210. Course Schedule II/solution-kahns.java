class Solution {
    private int visited = 2;
    private int visiting = 1;
    private int unvisited = 0;
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap<Integer, List<Integer>>();
        int[] inDegree = new int[numCourses];
        
        // get graph and indegree 
        setGraphAndIndegree(numCourses, prerequisites, graph, inDegree);
        
        // solution
        int[] topSort = new int[numCourses];
        int index = numCourses-1;
        
        // get 0 indegree node
        List<Integer> zeroIndegree = new ArrayList<Integer>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                zeroIndegree.add(i);
            }
        }
        
        // run through all zeroIndegree vertices
        int course;
        int count = 0;
        while (!zeroIndegree.isEmpty()) {
            course = zeroIndegree.remove(0);
            count++;
            topSort[index--] = course;
            List<Integer> adjList = graph.get(course);
            for (int prereq: adjList) {
                inDegree[prereq]--;
                if (inDegree[prereq] == 0) {
                    zeroIndegree.add(prereq);
                }
            }
        }

        // cannot complete courses
        if (count != numCourses) {
            return new int[0];
        }
        
        return topSort;
    }
    
    public Map<Integer, List<Integer>> setGraphAndIndegree(int numCourses, 
                                               int[][] prerequisites,
                                               Map<Integer, List<Integer>> graph,
                                               int[] inDegree) {
        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<Integer>());
            inDegree[i] = 0;
        }
        
        List<Integer> adjList;
        for (int[] edge: prerequisites) {
            adjList = graph.get(edge[0]);
            adjList.add(edge[1]);
            inDegree[edge[1]]++;
        }
        return graph;
    }
}
