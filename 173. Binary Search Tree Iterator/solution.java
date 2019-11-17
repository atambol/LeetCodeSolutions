/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    Stack<TreeNode> stack;
    TreeNode node;
    public BSTIterator(TreeNode root) {
        node = root;
        stack = new Stack<>();
        while (node != null) {
            stack.add(node);
            node = node.left;
        }
    }
    
    /** @return the next smallest number */
    public int next() {
        int sol;
        node = stack.pop();
        sol = node.val;
        node = node.right;
        while (node != null) {
            stack.add(node);
            node = node.left;
        }
        return sol;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
