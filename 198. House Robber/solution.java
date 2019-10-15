class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 0;
        }
        
        if (n == 1) {
            return nums[0];
        }
        
        int one = 0;
        int two = 0;
        int three;
        
        for (int i = 0; i < n; i++) {
            three = Math.max(one + nums[i], two);
            one = two;
            two = three;
        }
        
        return Math.max(one, two);
    }
}
