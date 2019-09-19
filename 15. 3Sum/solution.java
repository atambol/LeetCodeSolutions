class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        
        // edge case
        if (nums.length < 3) {
            return sol;
        }
        
        Arrays.sort(nums);
        int i, j, k;
        int total = 0;
        int len = nums.length;
        for(i = 0; i < len; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            j = i+1;
            k = len-1;
            
            while (j < k) {
                total = nums[i] + nums[j] + nums[k];
                if (total == 0) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(nums[i]);
                    tmp.add(nums[j]);
                    tmp.add(nums[k]);
                    sol.add(tmp);
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j-1]) {
                        j++;
                    }
                    while (j < k && nums[k] == nums[k+1]) {
                        k--;
                    }
                }
                else if (total < 0) {
                    j++;
                } 
                else {
                    k--;
                }
            }
        }
        return sol;
    }
}
