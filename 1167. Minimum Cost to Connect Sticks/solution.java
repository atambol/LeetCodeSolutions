class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(sticks.length);
        
        // insert all the heap
        for (Integer stick: sticks) {
            heap.add(stick);
        }
        
        // grab two, join them and put back until one stick is left
        int cost = 0;
        Integer stick;
        while (heap.size() > 1) {
            stick = heap.remove();
            stick += heap.remove();
            cost += stick;
            heap.add(stick);
        }
        
        return cost;
    }
}
