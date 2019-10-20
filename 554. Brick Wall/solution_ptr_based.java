class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        // edge case
        int n = wall.size();
        if (n == 0) {
            return 0;
        }
        
        if (n == 1) {
            if (wall.get(0).size() == 1) {
                return 1;
            } else {
                return 0;
            }
        }
        
        // create length sums for each row and pointer for each row
        int[] ptrs = new int[n];
        int[] totals = new int[n];
        for (int i = 0; i < n; i++) {
            ptrs[i] = 0;
            totals[i] = 0;
        }
        
        // get max width
        int width = 0;
        for (Integer w: wall.get(0)) {
            width += w;
        }
        
        // loop over each row and get the minSum
        int minSum = 0;
        int edges;
        int minEdges = n;
        while (minSum != width) {
            minSum = Integer.MAX_VALUE;
            
            // get the minSum
            for (int i = 0; i < n; i++) {
                if (width != totals[i]) {
                    minSum = Math.min(minSum, totals[i] + wall.get(i).get(ptrs[i]));
                }
            }
            // System.out.println(minSum);
            // count edges
            edges = n;
            if (minSum != Integer.MAX_VALUE) {
                for (int i = 0; i < n; i++) {
                    if ((minSum == totals[i] + wall.get(i).get(ptrs[i])) && (minSum != width)){
                        edges--;
                        totals[i] = minSum;
                        ptrs[i]++;
                    }
                }
            
                minEdges = Math.min(minEdges, edges);
            }
            // System.out.println(minEdges);
        }
        
        return minEdges;
    }
}
