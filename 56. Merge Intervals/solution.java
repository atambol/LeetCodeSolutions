class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        int i = 0;
        int j = 1;
        
        while (j < intervals.length) {
            if (intervals[i][1] >= intervals[j][0]) {
                intervals[i][1] = Math.max(intervals[i][1], intervals[j][1]);
            } else {
                i++;
                intervals[i][0] = intervals[j][0];
                intervals[i][1] = intervals[j][1];
            }
            j++;
        }
        
        i++;
        int[][] sol = new int[i][2];
        for (j = 0; j < i; j++) {
            sol[j][0] = intervals[j][0];
            sol[j][1] = intervals[j][1];
        }
        
        return sol;
    }
}
