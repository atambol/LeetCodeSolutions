class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sol = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0; i < nums.length; i++) {
            if (map.get(target - nums[i]) != null) {
                sol[0] = map.get(target - nums[i]);
                sol[1] = i;
                return sol;
            } else {
                map.put(nums[i], i);
            }
        }
        return sol;
    }
}
