class Solution {
    public int maxArea(int[] height) {
        int area = 0, maxArea = 0;
        int i = 0;
        int j = height.length-1;
        while (i < j) {
            area = Math.min(height[j], height[i])*(j-i);
            if (area > maxArea) {
                maxArea = area;
            }
            if (height[i] > height[j]) {
                j--;
            }
            else {
                i++;
            }
        }
        return maxArea;
    }
}
