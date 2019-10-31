class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int u;
        int v;
        DisjointSet ds = new DisjointSet();
        
        for (int i = 0; i < edges.length; i++) {
            u = edges[i][0];
            v = edges[i][1];
            
            if (ds.isNotPresent(u)) {
                ds.makeSet(u);
            }
            
            if (ds.isNotPresent(v)) {
                ds.makeSet(v);
            }
            
            if (ds.find(u) == ds.find(v)) {
                return edges[i];
            } else {
                ds.union(u, v);
            }
        }
        
        return edges[edges.length-1];
    }
    
    public class DisjointSet {
        private Map<Integer, Integer> parent;
        private Map<Integer, HashSet<Integer>> children;
        
        public DisjointSet () {
            parent = new HashMap<Integer, Integer>();
            children = new HashMap<Integer, HashSet<Integer>>();
        }
        
        public boolean isNotPresent(int v) {
            return !parent.containsKey(v);
        }        
        
        public void makeSet(int v) {
            parent.put(v, v);
            HashSet set = new HashSet<Integer>();
            set.add(v);
            children.put(v, set);
        }
        
        public int find(int v) {
            return parent.get(v);
        }
        
        public void union(int u, int v) {
            int p1 = find(u);
            int p2 = find(v);
            if (p1 != p2) {
                if (children.get(p1).size() > children.get(p2).size()) {
                    update(p1, p2);
                } else {
                    update(p2, p1);
                }
            }
        }
        
        public void update(int p1, int p2) {
            HashSet<Integer> c1 = children.get(p1);
            HashSet<Integer> c2 = children.get(p2);
            for (Integer c: c2) {
                c1.add(c);
                parent.put(c, p1);
            }
            
            c2.clear();
        }
    }
}
