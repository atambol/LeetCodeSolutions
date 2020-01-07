class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // get the frequency
        Map<String, Integer> freq = new HashMap<>();
        for (String word: words) {
            freq.put(word, freq.getOrDefault(word, 0)+1);
        }
        
        // sort them
        List<Node> nodes = new ArrayList<>();
        freq.forEach((u, v) -> nodes.add(new Node(v, u)));
        Collections.sort(nodes, new Comparator<Node>(){
            public int compare(Node n1, Node n2) {
                if (n1.f == n2.f) {
                    return n1.s.compareTo(n2.s);
                } else {
                    return n2.f - n1.f;
                }
            }
        });
        
        // final solution
        List<String> sol = new ArrayList<String>();
        for (int i = 0; i < k; i++) {
            sol.add(nodes.get(i).s);
        }
        
        return sol;
    }
    
    public class Node {
        public int f;
        public String s;
        public Node(int f, String s) {
            this.f = f;
            this.s = s;
        }
    }
}
