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
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, null, null);
    }
    
    public boolean isValidBST(TreeNode root, Integer left, Integer right) {
        if (root == null) {
            return true;
        }
        
        boolean isValid = true;
        
        if ((right != null) && (root.val >= right)) 
            isValid = false;
        if (isValid && (left != null) && (root.val <= left))
            isValid = false;
        if (isValid)
            return isValidBST(root.left, left, root.val) && isValidBST(root.right, root.val, right);
        else
            return false;
    }
}
