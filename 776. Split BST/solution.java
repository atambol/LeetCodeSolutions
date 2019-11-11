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
    public TreeNode[] splitBST(TreeNode root, int V) {
        if (root == null) 
            return new TreeNode[]{null, null};
        else if (root.val > V) {
            TreeNode[] left = splitBST(root.left, V);
            root.left = left[1];
            left[1] = root;
            return left;
        } else {
            TreeNode[] right = splitBST(root.right, V);
            root.right = right[0];
            right[0] = root;
            return right;
        }
    }
}
