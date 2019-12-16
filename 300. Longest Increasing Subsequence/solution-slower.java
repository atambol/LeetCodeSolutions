class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] count = new int[nums.length];
        int maxLength = 0;
        for (int i = 0; i < nums.length; i++) {
            if (count[i] == 0) {
                backtrack(nums, i, count);
            }
            maxLength = Math.max(maxLength, count[i]);
        }
        return maxLength;
    }
    
    public void backtrack(int[] nums, int start, int[] count) {
        // base case
        count[start] = 1;
        
        // other case
        for (int i = start+1; i < nums.length; i++) {
            if (nums[i] > nums[start]) {
                if (count[i] == 0) {
                    backtrack(nums, i, count);
                }
                count[start] = Math.max(count[start], count[i]+1);
            }
        }
    }
}
