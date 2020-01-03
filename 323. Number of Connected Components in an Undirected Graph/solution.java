class Solution {
    private int[] parent;
    public int find(int x) {
        if (parent[x] == x) {
            return x;
        } else {
            parent[x] = find(parent[x]);
            return parent[x];
        }
    }
    
    public void union(int x, int y) {
        int parentX = find(x);
        int parentY = find(y);
        if (parentX != parentY) {
            parent[parentY] = parentX;
        }
    }
    
    public int countComponents(int n, int[][] edges) {
        // init
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // union
        int count = 0;
        for (int[] edge: edges) {
            union(edge[0], edge[1]);
        }
        
        // count
        for (int i = 0; i < n; i++) {
            if (parent[i] == i){
                count++;
            }
        }
        
        return count;
    }
}
