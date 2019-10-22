class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> set = new HashSet<String>(wordDict);
        boolean[] visited = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
            visited[i] = false;
        }
        return wordBreak(s, 0, set, visited);
    }
    
    public boolean wordBreak(String s, int start, HashSet<String> set, boolean[] visited) {
        int n = s.length();
        visited[start] = true;
        
        for (int i = start; i < n; i++) {
            if (set.contains(s.substring(start, i+1))) {
                if (i + 1 == n) {
                    return true;
                }
                
                if (!visited[i+1] && wordBreak(s, i + 1, set, visited) == true) {
                    return true;
                }
            }
        }
        return false;
    }
}
