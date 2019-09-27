class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0;
        int maxSum = Integer.MIN_VALUE;
        
        for (int num: nums) {
            sum = Math.max(sum + num, num);
            maxSum = Math.max(sum, maxSum);
        }
        
        return maxSum;
    }
}
