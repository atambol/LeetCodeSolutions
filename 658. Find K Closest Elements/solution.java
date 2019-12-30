class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(k, new Comparator<int[]>() {
            public int compare(int[] n1, int[] n2) {
                if (n2[1] == n1[1]) {
                    return n2[0] - n1[0];
                }
                return n2[1] - n1[1];
            }
        });
        
        for (int a: arr) {
            heap.add(new int[]{a, Math.abs(a-x)});
            while (heap.size() > k) 
                heap.poll();
        }
        
        List<Integer> sol = new ArrayList<>();
        while (heap.size() > 0) {
            sol.add(heap.poll()[0]);
        }
        Collections.sort(sol);
        return sol;
    }
}
