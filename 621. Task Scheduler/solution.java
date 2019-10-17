class Solution {
    public int leastInterval(char[] tasks, int n) {
        // construct map
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (char task: tasks) {
            if (map.containsKey(task)) {
                map.put(task, map.get(task) + 1);
            } else {
                map.put(task, 1);
            }
        }
        
        // create heap
        PriorityQueue<Task> heap = new PriorityQueue<Task>(map.size(), (a, b) -> b.priority - a.priority);
        Task task;
        for (char t: map.keySet()) {
            task = new Task(t, map.get(t));
            heap.add(task);
        }
        
        // extract heap till empty
        int intervals = 0;
        List<Task> aux = new ArrayList<Task>(map.size());
        while (!heap.isEmpty()) {
            int i = n;
            while (!heap.isEmpty() && i >= 0) {
                task = heap.poll();
                task.priority--;
                if (task.priority > 0) {
                    aux.add(task);
                }
                intervals++;
                i--;
            }
            
            if (i >= 0 && !aux.isEmpty())
                intervals += i + 1;
            
            heap.addAll(aux);
            aux.clear();
        }
        return intervals;
    }
    
    class Task {
        private Integer priority;
        private Character id;
        
        public Task(Character t, Integer p) {
            id = t;
            priority = p;
        }
    }
}
