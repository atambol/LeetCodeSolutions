class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        return binarySearch(nums, target, 0, nums.length-1);
    }
    
    public int binarySearch(int[] nums, int target, int low, int high) {
        // base condition
        if (high - low == 2) {
            if (nums[high] == target) {
                return high;
            } else if (nums[low] == target) {
                return low;
            } else if (nums[low + 1] == target) {
                return low + 1;
            } else {
                return -1;
            }
        } else if (high - low == 1) {
            if (nums[high] == target) {
                return high;
            } else if (nums[low] == target) {
                return low;
            } else {
                return -1;
            }
        } else if (high == low) {
            if (nums[high] == target) {
                return high;
            } else {
                return -1;
            }
        }
        
        // divide and conquer
        int mid = (high + low)/2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > nums[low]) {
            if (target < nums[mid] && target >= nums[low]) {
                return binarySearch(nums, target, low, mid-1);
            } else {
                return binarySearch(nums, target, mid+1, high);
            }
        } else {
            if (target <= nums[high] && target > nums[mid]) {
                return binarySearch(nums, target, mid+1, high);
            } else {
                return binarySearch(nums, target, low, mid-1);
            }
        }
    }
}
