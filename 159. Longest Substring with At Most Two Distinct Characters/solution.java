class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        HashSet<Character> bucket = new HashSet<>();
        Character lastChar = null;
        Character c;
        int lastCharLen = 0;
        int len = 0;
        int maxLen = 0;
        int i = 0;
        while (i < s.length()) {
            c = s.charAt(i);
            if (bucket.size() < 2) {
                if (bucket.contains(c)) {
                    lastCharLen++;
                } else {
                    lastCharLen = 1;
                }
                lastChar = c;
                bucket.add(c);
            } else {
                if (bucket.contains(c)) {
                    if (lastChar == c) {
                        lastCharLen++;
                    } else {
                        lastChar = c;
                        lastCharLen = 1;
                    }
                } else {
                    bucket.clear();
                    bucket.add(lastChar);
                    bucket.add(c);
                    len = lastCharLen;
                    lastCharLen = 1;
                    lastChar = c;
                }
            }
            len++;
            maxLen = Math.max(len, maxLen);
            i++;
        }
        return maxLen;
    }
}
