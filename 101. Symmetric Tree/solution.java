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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        return myIsSymmetric(root.left, root.right);
    }
    
    public boolean myIsSymmetric(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return true;
        }
        
        if (root1 == null || root2 == null) {
            return false;
        }
        
        if (root1.val == root2.val) {
             return myIsSymmetric(root1.left, root2.right) && myIsSymmetric(root1.right, root2.left); 
        } else {
            return false;
        }
    }
}
