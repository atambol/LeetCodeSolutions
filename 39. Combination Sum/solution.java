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
            List<Integer> newSubsol = new ArrayList<Integer>();
            newSubsol.addAll(subsol);
            sol.add(newSubsol);
            return;
        }
        
        if (target < 0) {
            return;
        }
        
        List<Integer> newSubsol = new ArrayList<Integer>();
        newSubsol.addAll(subsol);
        
        for (int i = pos; i < candidates.length; i++) {
            newSubsol.add(candidates[i]);
            backtrack(candidates, target-candidates[i], i, sol, newSubsol);
            newSubsol.remove(newSubsol.size()-1);
        }
    }
}
