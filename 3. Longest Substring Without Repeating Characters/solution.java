class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() <= 1) {
            return s.length();
        }
        
        int len = 0;
        int j = 0;
        String key;
        HashMap<String, Integer> index = new HashMap();
        for (int i = 0; i < s.length(); i++) {
            key = Character.toString(s.charAt(i));
            if (index.containsKey(key) == true) {
                j = Math.max(j, index.get(key) + 1);
            }
            index.put(key, i);
            if (len < (i - j + 1)) {
                len = i - j + 1;
            }
        }
        return len;
    }
}
