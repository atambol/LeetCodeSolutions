class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] count = new int[26];
        for (int i = 0; i < 26; i++) {
            count[i] = 0;
        }
        
        int base = Character.getNumericValue('a');
        int index;
        for (int i = 0; i < s.length(); i++) {
            index = Character.getNumericValue(s.charAt(i)) - base;
            count[index]++;
        }
        
        for (int i = 0; i < t.length(); i++) {
            index = Character.getNumericValue(t.charAt(i)) - base;
            count[index]--;
        }
        
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
