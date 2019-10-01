class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] order = new int[numCourses];
        int ptr = 0;

        // initialise indegree and graph to null
        Integer[] inDegree = new Integer[numCourses];
        List<Integer>[] graph = new List[numCourses];
        for (Integer course = 0; course < numCourses; course++) {
            graph[course] = new ArrayList<Integer>();
            inDegree[course] = 0;
        }
        
        // read prereq and update
        for (int i = 0; i < prerequisites.length; i++) {
            // graph course -> prereqs
            graph[prerequisites[i][0]].add(prerequisites[i][1]);
            
            // calculate in-degree
            inDegree[prerequisites[i][1]]++;
        }
        
        // zero indegree list
        Deque<Integer> deque = new LinkedList<Integer>(); 
        for (int course = 0; course < numCourses; course++) {
            if (inDegree[course] == 0) {
                deque.add(course);
            }
        }
         
        int course;
        
        while (!deque.isEmpty()) {
            course = deque.removeFirst();
            for (Integer prereq: graph[course]) {
                inDegree[prereq]--;
                if (inDegree[prereq] == 0) {
                    deque.add(prereq);
                }
            }
            order[ptr] = course;
            ptr++;
        }
        
        if (ptr != numCourses) {
            return new int[0];
        } else {
            reverse(order);
            return order;
        }
    }
    
    public void reverse(int[] order) {
        int i = 0;
        int j = order.length - 1;
        int tmp;
        while (i < j) {
            tmp = order[i];
            order[i] = order[j];
            order[j] = tmp;
            i++;
            j--;
        }
    }
}
