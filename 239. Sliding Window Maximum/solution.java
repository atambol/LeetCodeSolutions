class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // edge case
        if (k == 0 || nums.length == 0) {
            return new int[]{};
        }
        
        LinkedList<Integer> buffer = new LinkedList<>();
        int[] sol = new int[nums.length - k + 1];
        int ptr = 0;
        int i;
        
        // fill first m elements
        for (i = 0; i < k; i++) {
            while (!buffer.isEmpty() && nums[buffer.getLast()] < nums[i]) {
                buffer.removeLast();
            }
            buffer.addLast(i);
        }
        sol[ptr++] = nums[buffer.getFirst()];
        
        // fill the next batches
        for (i = k; i < nums.length; i++) {
            while (!buffer.isEmpty() && i - buffer.getFirst() >= k) {
                buffer.removeFirst();
            }
            
            while (!buffer.isEmpty() && nums[buffer.getLast()] < nums[i]) {
                buffer.removeLast();
            }
            
            buffer.addLast(i);
            sol[ptr++] = nums[buffer.getFirst()];
        }
        
        return sol;
    }
}
