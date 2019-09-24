class Solution {
    public int trap(int[] height) {
        // edge case
        int vol = 0;
        if (height.length <= 2) {
            return vol;
        }
        
        int[] left = new int[height.length];
        int[] right = new int[height.length];
        int maxHeight = height[0];
        
        // look from left to right
        left[0] = 0;
        for(int i = 1; i < height.length; i++) {
            if (height[i] > maxHeight) {
                maxHeight = height[i];
                left[i] = 0;
            } else {
                left[i] = maxHeight - height[i];
            }
        }
        
        maxHeight = height[height.length-1];
        
        // look from left to right
        right[height.length-1] = 0;
        for(int i = height.length-2; i >= 0; i--) {
            if (height[i] > maxHeight) {
                maxHeight = height[i];
                right[i] = 0;
            } else {
                right[i] = maxHeight - height[i];
            }
        }
            
        // take the min of both views
        for(int i = 0; i < height.length; i++) {
            vol += Math.min(left[i], right[i]);
        }
        
        return vol;
    }
}
