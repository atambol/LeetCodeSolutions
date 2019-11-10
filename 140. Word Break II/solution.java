class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        // create a set
        Set<String> wordSet = new HashSet<String>();
        for (String w: wordDict) {
            wordSet.add(w);
        }
        
        // backtrack and gather all possible sentences
        ArrayList<String>[] memo = new ArrayList[s.length()]; 
        backtrack(s, 0, wordSet, memo);
        return memo[0];
    }
    
    public void backtrack(String s, int start, Set<String> wordSet,  ArrayList<String>[] memo) {
        memo[start] = new ArrayList<String>();
        for (int i = start + 1; i <= s.length(); i++) {
            if (wordSet.contains(s.substring(start, i))) {
                if (i != s.length()) {
                    if (memo[i] == null)
                        backtrack(s, i, wordSet, memo);
                    for (String str: memo[i]) {
                        memo[start].add(s.substring(start, i) + " " + str);
                    }
                } else {
                    memo[start].add(s.substring(start, i));
                }
            }
        }
    }
}
