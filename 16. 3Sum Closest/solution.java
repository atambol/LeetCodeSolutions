class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        
        int minDiff = Integer.MAX_VALUE;
        int sol = nums[0] + nums[1] + nums[2];
        int curDiff;
        int total;
        int i = 0;
        while (i < nums.length-2) {
            int j = i + 1;
            int k = nums.length-1;
            while (j < k) {
                total = nums[i] + nums[j] + nums[k];
                curDiff = Math.abs(total - target);
                if (curDiff < minDiff) {
                    minDiff = Math.abs(total - target);
                    sol = total;
                } else if (total > target) {
                    k--;
                } else {
                    j++;
                }
            }
            i++;
            while (i < nums.length-2 && nums[i] == nums[i-1]) {
                i++;
            }
        }
        return sol;
    }
}
