class MedianFinder {
    private PriorityQueue<Integer> lower;
    private PriorityQueue<Integer> upper;
    
    /** initialize your data structure here. */
    public MedianFinder() {
        lower = new PriorityQueue<Integer>((a, b) -> b - a);
        upper = new PriorityQueue<Integer>((a, b) -> a - b);
    }
    
    public void addNum(int num) {
        // insert the number in upper half first
        upper.add(num);
        
        // rebalance the size of lower == upper or lower - 1 == upper
        num = upper.remove();
        lower.add(num);
        
        if (lower.size() - 1 > upper.size()) {
            num = lower.remove();
            upper.add(num);
        }
    }
    
    public double findMedian() {
        if (lower.size() == 0) {
            return 0.0;
        }
        double sol = lower.peek();
        
        if (lower.size() == upper.size()) {
            sol += upper.peek();
            sol /= 2;
        }
        
        return sol;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
