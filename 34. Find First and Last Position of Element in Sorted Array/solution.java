class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] sol = new int[] {-1, -1};
        if (nums.length != 0) {
            binarySearch(nums, target, sol, 0, nums.length-1);
        }
        return sol;
    }
    
    public void binarySearch(int[] nums, int target, int[] sol, int low, int high) {
        if (low == high) {
            if (nums[low] == target) {
                saveSolution(sol, low);
            }
            return;
        } else if (low > high) {
            return;
        }
        
        int mid = (low + high)/2;
        
        if (nums[mid] == target) {
            saveSolution(sol, mid);
            binarySearch(nums, target, sol, low, mid-1);
            binarySearch(nums, target, sol, mid+1, high);
        }
        else if (nums[mid] > target) {
            binarySearch(nums, target, sol, low, mid-1);
        } else {
            binarySearch(nums, target, sol, mid+1, high);
        }
    }
    
    public void saveSolution(int[] sol, int pos) {
        if (sol[0] == -1) {
            sol[0] = pos;
            sol[1] = pos;
        } else {
            if (pos < sol[0]) {
                sol[0] = pos;
            } else if (pos > sol[1]) {
                sol[1] = pos;
            }
        }
    }
}
