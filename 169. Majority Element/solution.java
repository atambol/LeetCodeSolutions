class Solution {
    public int majorityElement(int[] nums) {
        int count = 1;
        int major = nums[0];
        
        for(int i = 1; i < nums.length; i++) {
            if (major == nums[i]) 
                count++;
            else
                count--;
            
            if (count == 0) {
                major = nums[i+1];
            }
        }
        
        return major;
    }
}
