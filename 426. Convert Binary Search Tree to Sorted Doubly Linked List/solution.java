/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return root;
        }
        
        Result r = join(root);
        r.head.left = r.tail;
        r.tail.right = r.head;
        return r.head;
    }
    
    public Result join(Node root) {
        if (root == null) {
            return new Result(null, null);
        } else if (root.left == null && root.right == null) {
            return new Result(root, root);
        } else if (root.left != null && root.right == null) {
            Result lr = join(root.left);
            lr.tail.right = root;
            root.left = lr.tail;
            lr.tail = root;
            return lr;
        } else if (root.right != null && root.left == null) {
            Result rr = join(root.right);
            rr.head.left = root;
            root.right = rr.head;
            rr.head = root;
            return rr;
        } else {
            Result lr = join(root.left);
            lr.tail.right = root;
            root.left = lr.tail;

            Result rr = join(root.right);
            rr.head.left = root;
            root.right = rr.head;
            
            rr.head = lr.head;
            return rr;
        }
    }
    
    class Result {
        Node head;
        Node tail;
        
        public Result(Node h, Node t) {
            head = h;
            tail = t;
        }
    }
}
