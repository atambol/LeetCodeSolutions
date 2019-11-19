class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        if (n == 0)
            return 1;
        
        // replace neg numbers by 0
        for (int i = 0; i < n; i++) {
            if (nums[i] < 0) 
                nums[i] = 0;
        }
        
        // mark seen number by marking their index number as negative
        int index;
        for (int i = 0; i < n; i++) {
            if (Math.abs(nums[i]) <= n && nums[i] != 0) {
                index = Math.abs(nums[i]) - 1;
                if (nums[index] == 0) {
                    nums[index] = -n-1;
                } else {
                    nums[index] = -1*Math.abs(nums[index]);
                }
            }
        }
        
        // check the first index that is not marked negative
        int i;
        for (i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                return i+1;
            }
        }
        
        return i+1;
    }
}
