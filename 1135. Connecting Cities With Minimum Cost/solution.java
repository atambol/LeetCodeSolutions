class Solution {
    private int[] parent;
    private int n;
    
    public void union(int x, int y) {
        if (find(x) != find(y)) {
            parent[find(y)] = find(x);
        }
        n--;
    }
    
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
            return parent[x];
        } else {
            return x;
        }
    }
    
    public int minimumCost(int N, int[][] connections) {
        Arrays.sort(connections, (a,b) -> a[2] - b[2]);
        n = N;
        
        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            parent[i] = i;
        }
        
        int cost = 0;
        for (int[] connection: connections) {
            int x = connection[0];
            int y = connection[1];
            if (find(x) != find(y)) {
                union(x, y);
                cost += connection[2];
            }
        }
        
        return n == 1?cost:-1;
    }
}
