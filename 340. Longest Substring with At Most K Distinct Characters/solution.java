class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> charCountMap = new HashMap<>();
        int i = 0;
        int len = 0;
        Character character;
        Integer count;
        for (int j = 0; j < s.length(); j++) {
            // add char at j
            character = s.charAt(j);
            count = charCountMap.getOrDefault(character, 0);
            count++;
            charCountMap.put(character, count);
            
            // remove until capacity is created
            while (charCountMap.size() > k) {
                character = s.charAt(i);
                count = charCountMap.get(character);
                count--;
                if (count == 0) {
                    charCountMap.remove(character);
                } else {
                    charCountMap.put(character, count);
                }
                i++;
            }
            
            // calculate window length
            len = Math.max(len, j - i + 1);
        }
        return len;
    }
}
