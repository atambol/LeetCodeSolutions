/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode successor = null;
        
        // reach the node
        while (root.val != p.val) {
            if (root.val > p.val) {
                successor = root;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        
        // reach the leftmost node in the right subtree if exists
        if (root.right != null) {
            root = root.right;
            while (root.left != null) {
                root = root.left;
            }
            successor = root;
        }
        
        return successor;
    }
}
