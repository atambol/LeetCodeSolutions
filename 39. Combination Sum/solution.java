class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        
        List<Integer> subsol = new ArrayList<Integer>();
        backtrack(candidates, target, 0, sol, subsol);
        return sol;
    }
    
    public void backtrack(int[] candidates, int target, int pos, List<List<Integer>> sol, List<Integer> subsol) {
        if (target == 0) {
            sol.add(new ArrayList<Integer>(subsol));
            return;
        }
        
        for (int i = pos; i < candidates.length; i++) {
            if (target-candidates[i] < 0) {
                return;
            }
            subsol.add(candidates[i]);
            backtrack(candidates, target-candidates[i], i, sol, subsol);
            subsol.remove(subsol.size()-1);
        }
    }
}
