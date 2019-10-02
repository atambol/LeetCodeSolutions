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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Result r = search(root, p, q);
        return r.node;
    }
    
    public Result search(TreeNode root, TreeNode p, TreeNode q) {
        Result s = new Result();
        if (root == null) {
            return s;
        }
        
        Result l = search(root.left, p, q);
        if (l.node != null) {
            return l;
        }
        Result r = search(root.right, p, q);
        if (r.node != null) {
            return r;
        }
        
        if (root.val == p.val) {
            s.foundp = true;
        } else if (root.val == q.val) {
            s.foundq = true;
        }
        
        s.foundp = s.foundp || l.foundp || r.foundp;
        s.foundq = s.foundq || l.foundq || r.foundq;
        if (s.foundp && s.foundq) {
            s.node = root;
        }
        
        return s;
    }
    
    class Result {
        boolean foundp;
        boolean foundq;
        TreeNode node;
        
        public Result() {
            foundp = false;
            foundq = false;
            node = null;
        }
    }
        

}
