class Solution {
    public int hammingDistance(int x, int y) {
        x = x ^ y;
        y = x;
        int count = 0;
        while (x != 0) {
            y = x;
            x = x>>1;
            x = x<<1;
            if (y != x) {
                count++;
            }
            x = x>>1;
        }
        return count;
    }
}
