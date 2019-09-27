class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> sol = new ArrayList<List<String>>();
        int[] posArr = new int[n];
        for (int i =0; i < n; i++) {
            posArr[i] = 0;
        }
        backtrack(sol, posArr, 0, n);
        return sol;
    }
    
    public void backtrack(List<List<String>> sol, int[] posArr, int pos, int n) {
        if (pos == n) {
            saveSol(posArr, n, sol);
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (isSafe(posArr, pos, i) == true) {
                posArr[pos] = i;
                backtrack(sol, posArr, pos+1, n);
                posArr[pos] = 0;
            }
        }
    }
    
    public boolean isSafe(int[] posArr, int pos, int value) {
        for (int i = 0; i < pos; i++) {
            if (i == pos || posArr[i] == value || Math.abs(i - pos) == Math.abs(posArr[i] - value)) {
                return false;
            }
        }
        return true;
    }
    
    public void saveSol(int[] posArr, int n, List<List<String>> sol) {
        List<String> intSol = new ArrayList<String>();
        
        for (int i = 0; i < n; i++) {
            char[] chars = new char[n];
            for (int j = 0; j < n; j++) {
                if (posArr[i] == j) {
                    chars[j] = 'Q';
                } else {
                    chars[j] = '.';
                }
            }
            
            intSol.add(new String(chars));
        }
        
        sol.add(intSol);
    }
}
