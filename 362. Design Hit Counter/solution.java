class HitCounter {
    private Deque<Integer> deque;
    
    /** Initialize your data structure here. */
    public HitCounter() {
        deque = new LinkedList<Integer>(); 
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        deque.addLast(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while (!deque.isEmpty() && timestamp - deque.peekFirst() >= 300) {
            deque.removeFirst();
        }
        
        return deque.size();
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
