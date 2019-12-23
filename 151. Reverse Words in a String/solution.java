class Solution {
    public String reverseWords(String s) {
        int n = s.length();
        if (n == 0) {
            return s;
        }
        
        int i = 0;
        int j = 0;
        List<String> sol = new ArrayList<String>();
        while (j < n) {
            while (i < n && s.charAt(i) == ' ') {
                i++;
                j++;
            }
            
            while (j < n && s.charAt(j) != ' ') {
                j++;
            }
            
            if (i < n) {
                sol.add(s.substring(i, j));
                i = j;
                j++;
            }
        }
        
        Collections.reverse(sol);
        return String.join(" ", sol);
    }
}
