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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> sol = new ArrayList<>();
        if (root == null)
            return sol;
        List<TreeNode> layer = new ArrayList<TreeNode>();
        layer.add(root);
        TreeNode node = null;
        List<TreeNode> aux = new ArrayList<TreeNode>(); 
        while (!layer.isEmpty()) {
            while(!layer.isEmpty()) {
                node = layer.remove(0);
                if (node.left != null) {
                    aux.add(node.left);
                }
                if (node.right != null) {
                    aux.add(node.right);
                }
            }
            if (node != null)
                sol.add(node.val);
            layer = aux;
            aux = new ArrayList<TreeNode>(); 
        }
        return sol;
    }
}
