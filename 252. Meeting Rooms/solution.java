class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] i1, int[] i2) {
                if (i2[0] == i1[0]) {
                    return i1[1] - i2[1];
                }
                return i1[0] - i2[0];
            }
        });
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i-1][1] > intervals[i][0]) {
                return false;
            }
        }
        
        return true;
    }
}
