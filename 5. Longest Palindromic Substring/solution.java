class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        
        // Edge case
        if (len <= 1) {
            return s;
        }
        
        int low = 0;
        int high = 1;
        
        int i, j, k;
        for (i=0; i < len; i++) {
            // split around i
            j = i - 1;
            k = i + 1;
            while (j >= 0 && k < len && s.charAt(j) == s.charAt(k)) {
                j--;
                k++;
            }
            j++;
            
            if (high - low < k - j) {
                high = k;
                low = j;
            }
            
            // split between i
            j = i;
            k = i + 1;
            while (j >= 0 && k < len && s.charAt(j) == s.charAt(k)) {
                j--;
                k++;
            }
            j++;
            
            if (high - low < k - j) {
                high = k;
                low = j;
            }
        }
    return s.substring(low, high);
    }
}
