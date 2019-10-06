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
    public TreeNode deleteNode(TreeNode root, int key) {
        
        // add a dummy node
        TreeNode node = new TreeNode(Integer.MAX_VALUE);
        node.left = root;
        root = node;
        node = root.left;
        TreeNode prev = root;
        
        // search for the key
        while (node != null) {
            if (node.val == key) {
                break;
            } else if (node.val > key) {
                prev = node;
                node = node.left;
            } else {
                prev = node;
                node = node.right;
            }
        }
        
        // key found
        if (node != null) {
            TreeNode tmp = null;
            
            if (node.left == null && node.right == null) {
                ;
            } else if (node.left == null && node.right != null) {
                tmp = node.right;
            } else if (node.left != null && node.right == null) {
                tmp = node.left;
            } else {
                tmp = node.right;
                while (tmp.left != null) {
                    tmp = tmp.left;
                }
                
                tmp.left = node.left;
                tmp = node.right;
            }
        
            if (prev.left == node) {
                prev.left = tmp;
            } else {
                prev.right = tmp;
            }
        }
        
        return root.left;
    }
}
