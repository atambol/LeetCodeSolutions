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
    public int countNodes(TreeNode root) {
        int count = 0;
        while (root != null) {
            if (getDepth(root.left) == getDepth(root.right)) {
                count += Math.pow(2, getDepth(root.left));
                root = root.right;
            } else {
                count += Math.pow(2, getDepth(root.right));
                root = root.left;
            }
        }
        return count;
    }
    
    public int getDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            return 1 + getDepth(root.left);
        }
    }
}
