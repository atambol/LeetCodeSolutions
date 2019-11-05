class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        int n = nums.length;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            visited[i] = false;
        }
        
        List<Integer> subSol;
        for (int i = 0; i < n; i++) {
            visited[i] = true;
            subSol = new ArrayList<Integer>();
            subSol.add(nums[i]);
            backtrack(nums, visited, n, subSol, sol);
            visited[i] = false;
        }
        
        return sol;
    }
    
    public void backtrack(int[] nums, boolean[] visited, int n, 
                          List<Integer> subSol, List<List<Integer>> sol) {
        if (subSol.size() == n) {
            sol.add(subSol);
            return;
        }
        
        List<Integer> subSubSol;
        for (int i = 0 ; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                subSubSol = new ArrayList<Integer>(subSol);
                subSubSol.add(nums[i]);
                backtrack(nums, visited, n, subSubSol, sol);
                visited[i] = false;
            }

        }
    }
}
