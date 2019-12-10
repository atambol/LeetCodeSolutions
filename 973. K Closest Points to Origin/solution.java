class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<Point> heap = new PriorityQueue<>(K, new Comparator<Point>(){
            @Override
            public int compare(Point p1, Point p2) {
                return p2.d - p1.d;
            }
        });
        
        Point p;
        for (int[] point: points) {
            p = new Point(point[0], point[1]);
            heap.add(p);
            while (heap.size() > K) 
                heap.poll();
        }
        
        int[][] sol = new int[K][2];
        int i = 0;
        for (Point point: heap) {
            sol[i++] = point.getPoints();
        }
        
        return sol;
    }
    
    public class Point {
        private int x;
        private int y;
        public int d;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
            this.d = x*x + y*y;
        }
        
        public int[] getPoints() {
            return new int[]{x, y};
        }
    }
}
