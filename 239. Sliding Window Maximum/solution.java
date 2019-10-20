class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // edge case
        if (nums.length == 0 || k == 0) {
            return new int[0];
        }
        
        int[] sol = new int[nums.length - k + 1];
        Deque<Integer> deque = new LinkedList<Integer>();
        
        // get the first window
        int i = 0;
        while (i < k) {
            while (!deque.isEmpty() && (nums[deque.peekLast()] < nums[i])) {
                deque.pollLast();
            }
            
            deque.addLast(i++);
        }
        
        // save solution for first window
        int j = 0;
        sol[j++] = nums[deque.peekFirst()];
        
        // keep the window moving
        while (i < nums.length) {            
            while (!deque.isEmpty() && (deque.peekFirst() + k <= i)) {
                deque.pollFirst();
            }
            
            while (!deque.isEmpty() && (nums[deque.peekLast()] < nums[i])) {
                deque.pollLast();
            }
            
            deque.addLast(i++);
            sol[j++] = nums[deque.peekFirst()];
        }
        
        return sol;
    }
}
