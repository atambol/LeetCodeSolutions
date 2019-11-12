class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> freq = new HashMap<String, Integer>();
        for (String word: words) {
            if (!freq.containsKey(word)) {
                freq.put(word, 0);
            }
            freq.put(word, freq.get(word)+1);
        }
        
        PriorityQueue<Node> heap = new PriorityQueue<>(freq.size(), new Comparator<Node> () {
            @Override
            public int compare(Node n1, Node n2) {
                if (n1.count == n2.count) {
                    return n2.word.compareTo(n1.word);
                } else {
                    return n1.count - n2.count;
                }
            }
        });
        for (Map.Entry<String,Integer> entry : freq.entrySet())  {
            heap.add(new Node(entry.getValue(), entry.getKey()));
            while (heap.size() > k) {
                heap.poll();
            }
        }
        
        List<String> sol = new ArrayList<String>();
        while (!heap.isEmpty()) {
            sol.add(heap.poll().word);
        }
        Collections.reverse(sol);
        return sol;
    }
    
    class Node {
        int count;
        String word;
        
        public Node(int c, String w) {
            count = c;
            word = w;
        }
    }
}
