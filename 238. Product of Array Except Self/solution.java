class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prod = new int[nums.length];
        
        // left to right
        prod[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            prod[i] = prod[i-1] * nums[i-1];
        }
        
        // right to left
        int runningProd = nums[nums.length-1];
        for (int i = nums.length - 2; i >= 0; i--) {
            prod[i] = prod[i] * runningProd;
            runningProd *= nums[i];
        }
        
        return prod;
    }
}
