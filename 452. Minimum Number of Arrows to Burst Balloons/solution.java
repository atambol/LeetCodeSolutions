class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0)
            return 0;
        int arrows = 0;
        Arrays.sort(points, (a, b) -> a[0]==b[0]?(a[1]-b[1]):a[0]-b[0]);
        int minEnd = Integer.MIN_VALUE;
        for (int[] point: points) {
            int start = point[0];
            int end = point[1];
            if (start > minEnd) {
                minEnd = end;
                arrows++;
            } else {
                minEnd = Math.min(minEnd, end);
            }
        }
        if (minEnd == Integer.MIN_VALUE) {
            arrows++;
        }
        return arrows;
    }
}
