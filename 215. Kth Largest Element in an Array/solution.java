class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(k);
        
        for (int i = 0; i < k; i++) {
            pq.add(nums[i]);
        }
        
        for (int i = k; i < nums.length; i++) {
            if (nums[i] > pq.peek()) {
                if (pq.size() == k) {
                    pq.remove();
                }
                pq.add(nums[i]);
            }
        }
        
        return pq.peek();
    }
}
