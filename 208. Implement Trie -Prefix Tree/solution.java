class Trie {
    private Node node;
    
    /** Initialize your data structure here. */
    public Trie() {
        node = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node ptr = node;
        int index;
        for (int i = 0; i < word.length(); i++) {
            index = ptr.getIndex(word.charAt(i));
            if (ptr.node[index] == null) {
                ptr.node[index] = new Node();
            }
            ptr = ptr.node[index];
        }
        
        ptr.eow = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node ptr = node;
        int index;
        for (int i = 0; i < word.length(); i++) {
            index = ptr.getIndex(word.charAt(i));
            if (ptr.node[index] == null) {
                return false;
            }
            ptr = ptr.node[index];
        }
        
        return ptr.eow;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node ptr = node;
        int index;
        for (int i = 0; i < prefix.length(); i++) {
            index = ptr.getIndex(prefix.charAt(i));
            if (ptr.node[index] == null) {
                return false;
            }
            ptr = ptr.node[index];
        }
        
        return true;
    }
    
    class Node {
        Node[] node;
        boolean eow;
        
        public Node() {
            node = new Node[26];
            for (int i = 0; i < 26; i++) {
                node[i] = null;
            }
            
            eow = false;
        }
        
        public int getIndex(char c) {
            return (int)c - 97;
        }
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
