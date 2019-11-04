class AutocompleteSystem {
    private int ASCIIOfa;
    private Trie root;
    private Trie currentRoot;
    private String prefix;
    
    public AutocompleteSystem(String[] sentences, int[] times) {
        ASCIIOfa = (int)'a';
        root = new Trie();
        currentRoot = root;
        prefix = "";
        
        // insert the historical records
        for (int i = 0; i < sentences.length; i++) {
            insert(sentences[i], times[i]);
        }
    }
    
    // input a character and get a list of hot strings 
    public List<String> input(char c) {
        // min heap to store hot strings
        PriorityQueue<HotString> heap = new PriorityQueue<HotString>(3, new Comparator<HotString>() {
            public int compare(HotString s1, HotString s2) {
                if (s2.count == s1.count) {
                    // lexicographic check
                    return s2.string.compareTo(s1.string);
                } else{
                    // count check
                    return s1.count - s2.count;
                }
                
            }
        });
        
        // reset character
        if (c == '#') {
            currentRoot.count += 1;
            currentRoot = root;
            prefix = "";
        } else {
            int index = getIndex(c);
            // if the character is in trie already
            if (currentRoot.chars[index] != null) {
                prefix += Character.toString(c);
                currentRoot = currentRoot.chars[index];
                dfs(prefix, currentRoot, heap);
            } 
            
            // if it is not, dont dfs
            else {
                currentRoot.chars[index] = new Trie();
                currentRoot = currentRoot.chars[index];
            }
        }
        
        // extract solution
        List<String> sol = new ArrayList<String>();
        while (!heap.isEmpty()) {
            sol.add(heap.remove().string);
        }
        
        // since we use min heap, reverse the results
        Collections.reverse(sol);
        return sol;
    }
    
    // insert a sentence and its hit rate into the trie (during init only)
    public void insert(String sentence, int times) {
        Trie ptr = root;
        Integer index;
        for (int i = 0; i < sentence.length(); i++) {
            index = getIndex(sentence.charAt(i));
            if (ptr.chars[index] == null) {
                ptr.chars[index] = new Trie();
            }
            ptr = ptr.chars[index];
        }
        
        ptr.count = times;
    }

    // perform a dfs and extract top 3 hot Strings from the subTree
    public void dfs(String prefix, Trie node, PriorityQueue<HotString> heap) {
        if (node.count > 0) {
            HotString hotString = new HotString(prefix, node.count);
            heap.add(hotString);
            while (heap.size() > 3) {
                heap.poll();
            }
        }
        
        for (int i = 0; i < 27; i++) {
            if (node.chars[i] != null) {
                dfs(prefix + getChar(i), node.chars[i], heap);
            }
        }
    }

    // given a character, get its index within the chars array
    private int getIndex(char c) {
        if (c == ' ') {
            return 26;
        } else {
            return (int)c - ASCIIOfa;
        }
    }
    
    // given an index within the chars array, get its character
    private String getChar(int i) {
        char c;
        if (i == 26) {
            c = ' ';
        } else {
            c = (char) (i + ASCIIOfa);
        }
        return Character.toString(c);
    }
    
    // Trie class to store characters and their counts
    public class Trie {
        public Trie[] chars;
        public int count;
        
        public Trie() {
            chars = new Trie[27];
            for (int i = 0; i < 27; i++) {
                chars[i] = null;
            }
            count = 0;
        }
    }
    
    // HotString class used by the Priority queue
    public class HotString {
        public String string;
        public Integer count;
        
        public HotString(String s, Integer c) {
            string = s;
            count = c;
        }
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */
