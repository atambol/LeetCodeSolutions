class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length;
        int num;
        for (int i = 0; i < n; i++) {
            num = Math.abs(nums[i]);
            if (nums[num-1] < 0) {
                return num;
            } else {
                nums[num-1] *= -1;
            }
        }
        return nums[n-1];
    }
}
