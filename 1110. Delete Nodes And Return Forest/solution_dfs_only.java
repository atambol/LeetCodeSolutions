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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        List<TreeNode> roots = new ArrayList<>();
        if (root == null) 
            return roots;
        
        // create toDelete set
        Set<Integer> toDelete = new HashSet<Integer>();
        for (int val: to_delete) {
            toDelete.add(val);
        }
        
        // for dfs
        if (!toDelete.contains(root.val))
            roots.add(root);
        dfs(root, toDelete, roots);
        return roots;
    }
    
    public TreeNode dfs(TreeNode root, Set<Integer> toDelete, List<TreeNode> roots) {
        if (root == null) 
            return null;
        
        TreeNode left, right;
        left = dfs(root.left, toDelete, roots);
        right = dfs(root.right, toDelete, roots);
        
        if (toDelete.contains(root.val)) {
            if (left != null)
                roots.add(left);
            if (right != null) 
                roots.add(right);
            // root.left = null;
            // root.right = null;
            return null;
        } else {
            root.left = left;
            root.right = right;
            return root;
        }
    }
}
