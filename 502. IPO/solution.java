class Solution {
    public int findMaximizedCapital(int k, int W, int[] Profits, int[] Capital) {
        int n = Profits.length;
        
        // max heap
        PriorityQueue<Project> doableProjects = new PriorityQueue<Project>(n, new Comparator<Project>() {
    public int compare(Project p, Project q) {
        if (p.profit == q.profit) {
            return q.capital - p.capital;
        }
        
        return q.profit - p.profit;
    }
});
        
        // min heap
        PriorityQueue<Project> potentialProjects = new PriorityQueue<Project>(n, new Comparator<Project>() {
    public int compare(Project p, Project q) {
        if (p.capital == q.capital) {
            if (p.output == q.output) {
                return p.profit - q.profit;
            }
            return q.output - p.output;
        }
        
        return p.capital - q.capital;
    }
});
    
        // add projects to the heap
        Project project;
        for (int i = 0; i < n; i++) {
            project = new Project(Profits[i], Capital[i]);
            if (project.capital > W) {
                potentialProjects.add(project);
            } else {
                doableProjects.add(project);
            }
        }
        
        // extract the max output
        while (k != 0) {
            k--;
            
            // add all potential projects whose capital is no more than W to doable projects
            while (!potentialProjects.isEmpty() && potentialProjects.peek().capital <= W) {
                project = potentialProjects.poll();
                doableProjects.add(project);
            }
            
            // finish one project
            if (!doableProjects.isEmpty()) {
                W += doableProjects.poll().profit;
            } else {
                break;
            }               
        } 
        
        return W;
    }
    
    class Project {
        private int profit;
        private int capital;
        private int output;
        
        public Project(int p, int c) {
            profit = p;
            capital = c;
            output = p-c;
        }
    }
}
