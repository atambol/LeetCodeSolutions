class Solution {
    public boolean search(int[] nums, int target) {
        if (nums.length == 0) {
            return false;
        }
        return binarySearch(nums, target, 0, nums.length-1);
    }
    
    public boolean binarySearch(int[] nums, int target, int low, int high) {
        // base condition
        if (high - low == 2) {
            if (nums[high] == target) {
                return true;
            } else if (nums[low] == target) {
                return true;
            } else if (nums[low + 1] == target) {
                return true;
            } else {
                return false;
            }
        } else if (high - low == 1) {
            if (nums[high] == target) {
                return true;
            } else if (nums[low] == target) {
                return true;
            } else {
                return false;
            }
        } else if (high == low) {
            if (nums[high] == target) {
                return true;
            } else {
                return false;
            }
        }
        
        // divide and conquer
        int mid = (high + low)/2;
        if (nums[mid] == target) {
            return true;
        } 
        
        // the comparison below relies on the fact that it can decisively find 
        // the unrotated half in the rotated array by comparing low, mid and high
        // if elements repeat among low, mid or high, this cannot be found clearly
        // In such a case, linear search on both halves 
        else if (nums[low] == nums[high] || nums[low] == nums[mid] || nums[high] == nums[mid]) {
            return binarySearch(nums, target, low, mid-1) ||
                binarySearch(nums, target, mid+1, high);
            
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
