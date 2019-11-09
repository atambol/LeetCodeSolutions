class Solution {
    public String licenseKeyFormatting(String S, int K) {
        StringBuilder sol  = new StringBuilder();
        StringBuilder batch;
        int n = S.length();
        
        Character c;
        int i = n - 1;
        while (i >= 0) {
            batch = new StringBuilder();
            int j = 0;
            while (j < K && i >= 0) {
                if (S.charAt(i) != '-') {
                    c = S.charAt(i);
                    if (Character.isLowerCase(c)) {
                        c = Character.toUpperCase(c);
                    }
                    j++;
                    batch.append(c);
                }
                i--;

            }
            if (batch.length() != 0 && sol.length() != 0) {
                sol.append(new String("-"));
            }
            sol.append(batch.toString());
        }
        sol.reverse();
        return sol.toString();
    }
}
