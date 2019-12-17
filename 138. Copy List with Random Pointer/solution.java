/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    public Map<Node, Node> OldToNew = new HashMap<Node, Node>();
    public Node copyRandomList(Node head) {
        if (head == null) 
            return head;
        
        Node newHead = new Node();
        Node newNode = newHead;
        newHead.val = head.val;
        Node node = head.next;
        OldToNew.put(head, newHead);
        while (node != null) {
            newNode.next = new Node();
            newNode = newNode.next;
            newNode.val = node.val;
            OldToNew.put(node, newNode);
            node = node.next;
        }
        
        node = head;
        newNode = newHead;
        while (node != null) {
            if (node.random != null)
                newNode.random = OldToNew.get(node.random);
            newNode = newNode.next;
            node = node.next;
        }
        
        return newHead;
    }
}
