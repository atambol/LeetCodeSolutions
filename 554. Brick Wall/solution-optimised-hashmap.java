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
        
        // get max width
        int width = 0;
        for (Integer w: wall.get(0)) {
            width += w;
        }
        
        // create hashmap for each row's running sum
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sum;
        int count;
        int edges = n;
        for (int i = 0; i < n; i++) {
            sum = 0;
            for (Integer len: wall.get(i)) {
                sum += len;
                if (sum != width) {
                    count = map.getOrDefault(sum, 0) + 1;
                    map.put(sum, count);
                    edges = Math.min(edges, n - count);
                }
            }
        }
        return edges;
    }
}
