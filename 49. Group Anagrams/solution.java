class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        String key;
        List<String> anagrams;
        List<List<String>> allAnagrams = new ArrayList<List<String>>();
        Map<String, List<String>> anagramMap = new HashMap<String, List<String>>();
        for (String str: strs) {
            key = getCharCountKey(str);
            if (!anagramMap.containsKey(key)) {
                anagrams = new ArrayList<>();
                anagramMap.put(key, anagrams);
                allAnagrams.add(anagrams);
            } else {
                anagrams = anagramMap.get(key);
            }
            anagrams.add(str);
        }
        
        return allAnagrams;
    }
    
    public String getCharCountKey(String s) {
        int[] charCount = new int[26];
        int pos;
        for (int i = 0; i < s.length(); i++) {
            pos = (int)s.charAt(i) - (int)'a';
            charCount[pos]++;
        }
        
        StringBuilder key = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            key.append(Integer.toString(charCount[i]));
            key.append(new String("-"));
        }
        
        return key.toString();
    }
}
