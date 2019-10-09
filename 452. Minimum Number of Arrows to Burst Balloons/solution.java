class Solution {
    public int findMinArrowShots(int[][] points) {
        int arrows = 0;
        if (points.length == 0) {
            return arrows;
        }
        
        // sort
        Arrays.sort(points, (a, b) -> a[0] - b[0]);
        
        // count
        int end;
        int i = 0;
        while (i < points.length) {
            end = points[i][1];
            i++;
            while (i < points.length && points[i][0] <= end) {
                end = Math.min(end, points[i][1]);
                i++;
            }
            arrows++;
        }
        
        return arrows;
    }
}
