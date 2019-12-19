class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        List<Pair> pairs = new ArrayList<>(workers.length*bikes.length);
        
        Pair pair;
        for (int i = 0; i < workers.length; i++) {
            for (int j = 0; j < bikes.length; j++) {
                pair = new Pair(getManhattanDistance(workers[i], bikes[j]), i, j);
                pairs.add(pair);
            }
        }
        
        Collections.sort(pairs, new Comparator<Pair>() {
            public int compare(Pair p1, Pair p2) {
                if (p2.distance == p1.distance) {
                    if (p1.worker == p2.worker) {
                        return p1.bike - p2.bike;
                    }
                    return p1.worker - p2.worker;
                }
                return p1.distance - p2.distance;
            }
        });

        int[] visited = new int[bikes.length];
        int[] solution = new int[workers.length];
        Arrays.fill(solution, -1);
        for (Pair p: pairs) {
            if (visited[p.bike] == 0 && solution[p.worker] == -1) {
                visited[p.bike] = 1;
                solution[p.worker] = p.bike;
            }
        }
        
        return solution;
    }
    
    public int getManhattanDistance(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
    
    public class Pair {
        public int distance;
        public int worker;
        public int bike;
        
        public Pair(int d, int w, int b) {
            distance = d;
            worker = w;
            bike = b;
        }
    }
}
