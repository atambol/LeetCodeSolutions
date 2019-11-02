class Solution {
    public int[] getModifiedArray(int n, int[][] updates) {
        int[] corners = new int[n+1];
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            corners[i] = 0;
            array[i] = 0;
        }
        for (int[] update: updates) {
            corners[update[0]] += update[2];
            corners[update[1]+1] -= update[2];
        }
        
        // running sum
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += corners[i];
            array[i] = sum;
        }
        
        return array;
    }
}
