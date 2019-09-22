class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> sol = new ArrayList<>();
        
        if (n == 0) {
            return sol;
        }
        backtrack(n, 0, 0, "", sol);
        return sol;
    }
    
    public void backtrack(int n, int open, int close, String prefix, List<String> sol) {
        if (open == close && open == n) {
            sol.add(prefix);
            return;
        }
        
        if (open < n) {
            backtrack(n, open+1, close, prefix + "(", sol);
        }
        
        if (close < open) {
            backtrack(n, open, close+1, prefix + ")", sol);
        }
    }
}
