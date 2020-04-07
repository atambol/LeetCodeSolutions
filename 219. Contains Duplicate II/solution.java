class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        if (nums.length == 0 || k == 0) 
            return false;
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            } else {
                if (set.size() >= k) {
                    set.remove(nums[i-k]);
                }
                set.add(nums[i]);
            }
        }
        return false;
    }
}
