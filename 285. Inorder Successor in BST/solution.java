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
        // find the node
        TreeNode prev = null;
        while (root != null && root.val != p.val) {
            if (root.val > p.val) {
                prev = root;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        
        // successor
        if (root == null) {
            return root;
        }
        
        if (root.right != null) {
            root = root.right;
            while (root.left != null) {
                root = root.left;
            }
            return root;
        } else {
            return prev;
        }
    }
}
