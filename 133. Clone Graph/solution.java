/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
    public HashMap<Node, Node> visited = new HashMap<Node, Node>();
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        
        Node clone = new Node(node.val);
        clone.neighbors = new ArrayList<Node>();
        visited.put(node, clone);
        for (Node neigh: node.neighbors) {
            if (neigh != null) {
                if (visited.containsKey(neigh)) {
                    clone.neighbors.add(visited.get(neigh));
                } else {
                    clone.neighbors.add(cloneGraph(neigh));
                }
            }
        }
        return clone;
    }
}
