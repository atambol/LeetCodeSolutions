class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        // get freq
        HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (freq.containsKey(nums[i])) {
                freq.put(nums[i], freq.get(nums[i]) + 1);
            } else {
                freq.put(nums[i], 1);
            }
        }
        
        // create a heap of size k
        Freq f;
        PriorityQueue<Freq> heap = new PriorityQueue<Freq>(k, (a,b) -> a.count - b.count);
        for (Map.Entry<Integer,Integer> entry : freq.entrySet()) {
            f = new Freq(entry.getKey(), entry.getValue());
            if (heap.size() < k) {
                heap.add(f);
            }
            else if (heap.peek().count < f.count ) {
                heap.poll();
                heap.add(f);
            }
        }
        
        // extract the elements
        List<Integer> sol = new ArrayList<Integer>(heap.size());
        while (!heap.isEmpty()) {
            f = heap.poll();
            sol.add(f.num);
        }
        
        return sol;
    }
    
    class Freq {
        int num;
        int count;
        
        public Freq(int n, int f) {
            num = n;
            count = f;
        }
    }
}
