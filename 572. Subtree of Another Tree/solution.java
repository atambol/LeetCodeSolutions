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
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (t == null && s == null)
            return true;
        else if (t == null || s == null)
            return false;
        else if (t.val != s.val)
            return isSubtree(s.left, t) || isSubtree(s.right, t);
        else
            return isSame(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    public boolean isSame(TreeNode s, TreeNode t) {
        if (t == null && s == null)
            return true;
        else if (t == null || s == null)
            return false;
        else if (t.val != s.val)
            return false;
        else
            return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}
