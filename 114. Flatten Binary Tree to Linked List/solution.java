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
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        myFlatten(root);
    }
    
    public TreeNode myFlatten(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root;
        } else if (root.left != null && root.right == null) {
            TreeNode tail = myFlatten(root.left);
            root.right = root.left;
            root.left = null;
            return tail;
        } else if (root.left == null && root.right != null) {
            TreeNode tail = myFlatten(root.right);
            return tail;
        } else {
            TreeNode leftTail = myFlatten(root.left);
            TreeNode rightTail = myFlatten(root.right);
            leftTail.right = root.right;
            root.right = root.left;
            root.left = null;
            return rightTail;
        }
    }
}
