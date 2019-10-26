class Solution {
    public int nthUglyNumber(int n) {
        if (n == 0) {
            return 0;
        }
        
        if (n == 1) {
            return 1;
        }
        
        int[] ugly = new int[n];
        int x = 0;
        int y = 0;
        int z = 0;
        int i = 0;
        ugly[i] = 1;
        i++;
        while (i < n) {
            ugly[i] = Math.min(ugly[x]*2, Math.min(ugly[y]*3, ugly[z]*5));
            if (ugly[i] == ugly[x]*2) {
                x++;
            } else if (ugly[i] == ugly[y]*3) {
                y++;
            } else {
                z++;
            } 
            
            if (ugly[i] > ugly[i-1]) {
                i++;
            }
        }
        return ugly[i-1];
    }
}
