class Solution {
    public int maximalSquare(char[][] matrix) {
        // edge cases
        int m = matrix.length;
        if (m == 0) {
            return 0;
        }
        int n = matrix[0].length;
        if (n == 0) {
            return 0;
        }
        
        // initialise two matrix to store intermediate results
        int area = 0;
        int[][] height = new int[m][n];
        int[][] width = new int[m][n];
        
        // 0, 0
        if (matrix[0][0] == '1') {
            height[0][0] = 1;
            width[0][0] = 1;
            area = 1;
        } else {
            height[0][0] = 0;
            width[0][0] = 0;
        }
        
        // first column
        for (int i = 1; i < m; i++) {
            if (matrix[i][0] == '1') {
                height[i][0] = 1;
                width[i][0] = 1;
                area = 1;
            } else {
                height[i][0] = 0;
                width[i][0] = 0;
            }
        }

        // first row
        for (int i = 1; i < n; i++) {
            if (matrix[0][i] == '1') {
                height[0][i] = 1;
                width[0][i] = 1;
                area = 1;
            } else {
                height[0][i] = 0;
                width[0][i] = 0;
            }
        }

        // track the largest square
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    height[i][j] = Math.min(height[i-1][j-1], height[i-1][j]) + 1;
                    width[i][j] = Math.min(width[i-1][j-1], width[i][j-1]) + 1;
                    
                    area = Math.max(Math.min(height[i][j], width[i][j])*Math.min(height[i][j], width[i][j]), area);
                } else {
                    height[i][j] = 0;
                    width[i][j] = 0;
                }
            }
        }
        
        // for (int i = 0; i < m; i++) {
        //     for (int j = 0; j < n; j++) {
        //         System.out.printf("%d, %d\t", height[i][j], width[i][j]);
        //     }
        //     System.out.printf("\n");
        // }

        return area;
    }
}
