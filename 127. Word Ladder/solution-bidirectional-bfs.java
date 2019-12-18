class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        wordList.add(beginWord);
        Map<String, Set<String>> transformableWords = getTransformableWords(wordList);
        if (!transformableWords.containsKey(endWord))
            return 0;
        
        return bfs(transformableWords, beginWord, endWord);
    }
    
    public int bfs(Map<String, Set<String>> transformableWords, String beginWord, String endWord) {
        // start bfs from both ends
        int wordCount = transformableWords.size();
        
        // layers containing the current fanout
        Set<String> l1 = new HashSet<String>();
        Set<String> l2 = new HashSet<String>();
        
        // visited set for each end
        Set<String> v1 = new HashSet<String>(wordCount);
        Set<String> v2 = new HashSet<String>(wordCount);
        
        // depth for both ends
        int d1 = 0, d2 = 0;
        
        // init
        l1.add(beginWord);
        // v1.add(beginWord);
        l2.add(endWord);
        // v2.add(endWord);
        
        // run bfs
        while (l1.size()*l2.size() != 0) {
            l1 = getNextLayer(l1, v1, transformableWords);
            d1++;
            
            if (compareLayer(l1, l2)) {
                return d1 + d2 + 1;
            }
            
            l2 = getNextLayer(l2, v2, transformableWords);
            d2++;
            
            if (compareLayer(l1, l2)) {
                return d1 + d2 + 1;
            }            
        }
        
        return 0;
    }
    
    public Set<String> getNextLayer(Set<String> layer, Set<String> visited, Map<String, Set<String>> transformableWords) {
        Set<String> nextLayer = new HashSet<>();
        for (String word: layer) {
            visited.add(word);
            for (String neigh: transformableWords.get(word)) {
                if (!visited.contains(neigh))
                    nextLayer.add(neigh);
            }
        }
        return nextLayer;
    }
    
    public boolean compareLayer(Set<String> l1, Set<String> l2) {
        for (String word: l1) {
            if (l2.contains(word))
                return true;
        }
        return false;
    }
    
    public Map<String, Set<String>> getTransformableWords(List<String> wordList) {
        Map<String, Set<String>> wordToTransformations = new HashMap<String, Set<String>>();
        Set<String> trans;
        for (String word: wordList) {
            trans = new HashSet<String>();
            wordToTransformations.put(word, trans);
        }
        
        String word1, word2;
        for (int i = 0; i < wordList.size(); i++) {
            word1 = wordList.get(i);
            for (int j = i+1; j < wordList.size(); j++) {
                word2 = wordList.get(j);
                if (isOneEditTransformable(word1, word2)) {
                    trans = wordToTransformations.get(word1);
                    trans.add(word2);
                    trans = wordToTransformations.get(word2);
                    trans.add(word1);
                }
            }
        }
        return wordToTransformations;
    }
    
    public boolean isOneEditTransformable(String word1, String word2) {
        int count = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i))
                count++;
            
            if (count > 1) 
                return false;
        }
        
        if (count == 1)
            return true;
        else 
            return false;
    }
}
