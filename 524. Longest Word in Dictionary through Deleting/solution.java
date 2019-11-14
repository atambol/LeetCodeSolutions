class Solution {
    public String findLongestWord(String s, List<String> d) {
        // sort the list d by largest size first and lexicographically next
        Collections.sort(d, new Comparator<String>() {
            @Override
            public int compare(String s, String t) {
                if (s.length() > t.length()) {
                    return -1;
                } else if (t.length() > s.length()) {
                    return 1;
                } else {
                    return s.compareTo(t);
                }
            }
        });
        
        // pick a word and look for it in s
        for(String word: d) {
            int i = 0;
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == word.charAt(i)) {
                    i++;
                }
                if (word.length() == i) {
                    return word;
                }
            }
        }

        return "";
    }
}
