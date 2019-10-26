class Solution {
    public int singleNumber(int[] nums) {
        int xor = 0;
        for (int i = 0; i < nums.length; i++) {
            xor ^= nums[i];
        }
        
        for (int i = 0; i < nums.length; i++) {
            if ((xor ^ nums[i]) == 0) {
                return nums[i];
            }
        }
        return -1;
    }
}
