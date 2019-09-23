class Solution {
    public void nextPermutation(int[] nums) {
        // edge cases
        if (nums.length <= 2) {
            reverse(nums, 0);
            return;
        }
        
        // find the first decreasing element from right
        int pos = -1;
        for (int i = nums.length-2; i >= 0; i--) {
            if (nums[i+1] > nums[i]) {
                pos = i;
                break;
            }
        }
        
        // if no such position, reverse and return
        if (pos == -1) {
            reverse(nums, 0);
            return;
        }
        
        // find the least largest number on the right
        int larger = pos+1;
        for (int i = pos+2; i < nums.length; i++) {
            if (nums[i] > nums[pos] && nums[i] <= nums[larger]) {
                larger = i;
            }
        }
        
        // swap the numbers
        int tmp = nums[pos];
        nums[pos] = nums[larger];
        nums[larger] = tmp;
        
        reverse(nums, pos + 1);
    }
    
    public void reverse(int[] nums, int start) {
        int tmp;
        for (int i = start, j = nums.length - 1; i < j; i++, j--) {
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
}
