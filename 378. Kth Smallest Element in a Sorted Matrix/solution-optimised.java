class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        
        // search space is the entire matrix
        int low = matrix[0][0];
        int high = matrix[n-1][n-1];
        int mid;
        int count;
        
        while (low < high) {
            mid = (high+low)/2;
            
            // initial search space
            int[] minMax = new int[] {low, high};
    
            // get count of numbers less than mid
            count = countLessThan(matrix, mid, minMax);
            
            // return of kth element is found
            if (count == k)
                return minMax[0];
            
            // reduce search space otherwise (sort of like binary search)
            else if (count < k) 
                low = minMax[1];
            else
                high = minMax[0];
        }
        
        return low;
    }
    
    public int countLessThan(int[][] matrix, int mid, int[] minMax) {
        int n = matrix.length;
        int count = 0;
        
        // start at bottom left
        int i = n - 1;
        int j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] > mid) {
                minMax[1] = Math.min(matrix[i][j], minMax[1]);
                i--;
            } else {
                minMax[0] = Math.max(matrix[i][j], minMax[0]);
                j++;
                count += i + 1;
            }
        }
        return count;
    }
}
