class Solution {
    public int climbStairs(int n) {
        int step1 = 1;
        if (n == 1) {
            return step1;
        }
        
        int step2 = 2;
        if (n == 2) {
            return step2;
        }
        
        n -= 2;
        
        while (n > 0) {
            step2 = step2 + step1;
            step1 = step2 - step1;
            n--;
        }
        
        return step2;
    }
}
