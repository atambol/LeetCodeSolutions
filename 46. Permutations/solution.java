class Solution {
    public List<List<Integer>> permute(int[] nums) {
        Set<Integer> visited = new HashSet<Integer>();
        return backtrack(nums, visited);
    }
    
    public List<List<Integer>> backtrack(int[] nums, Set<Integer> visited) {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if (nums.length == visited.size()) {
            sol.add(new ArrayList<Integer>());
            return sol;
        } else {
            for (int num: nums) {
                if (!visited.contains(num)) {
                    visited.add(num);
                    List<List<Integer>> subSol = backtrack(nums, visited);
                    for (List<Integer> s: subSol) {
                        s.add(num);
                        sol.add(s);
                    }
                    visited.remove(num);
                }
            }
        }
        
        return sol;
    }
}
