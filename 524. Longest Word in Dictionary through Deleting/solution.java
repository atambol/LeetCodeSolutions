class Solution {
    private String nullString = new String("");
    public String findLongestWord(String s, List<String> d) {
        TrieNode root = new TrieNode();
        for (String S: d) {
            insert(root, S);
        }
        
        String sol = new String("");
        String candidate;
        int end;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            candidate = find(root, s, i, "");
            sol = compareAndGet(candidate, sol);
        }
        
        return sol;
    }
    
    public class TrieNode {
        public TrieNode[] nodes;
        public boolean eow;
        
        public TrieNode() {
            nodes = new TrieNode[26];
            for (int i = 0; i < 26; i++) {
                nodes[i] = null;
            }
            eow = false;
        }
    }
    
    public void insert(TrieNode root, String s) {
        int index;
        for (int i = 0; i < s.length(); i++) {
            index = getIndex(s.charAt(i));
            if (root.nodes[index] == null) {
                root.nodes[index] = new TrieNode();
            }
            root = root.nodes[index];
        }
        root.eow = true;
    }
    
    public String find(TrieNode root, String s, int i, String prefix) {
        String sol = (root.eow) ? prefix: nullString;
        if (i == s.length()) {
            return sol;
        }
    
        int index = getIndex(s.charAt(i));
        if (root.nodes[index] != null) {
            sol = compareAndGet(sol, find(root.nodes[index], s, i+1, prefix + s.substring(i, i+1))); 
            sol = compareAndGet(sol, find(root, s, i+1, prefix));
        } else {
            sol = compareAndGet(sol, find(root, s, i+1, prefix));
        }
        
        return sol;
    }
    
    public int getIndex(char c) {
        return (int)c - 97;
    }
    
    public String compareAndGet(String s, String t) {
        if (s.length() > t.length()) {
            return s;
        } else if (t.length() > s.length()) {
            return t;
        } else {
            if (s.compareTo(t) > 0) {
                return t;
            } else {
                return s;
            }
        }
    }
}
