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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<TreeNode> q = new ArrayList<TreeNode>();
        List<TreeNode> newQ;
        List<Integer> subSol;
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if (root == null) {
            return sol;
        }
        boolean reverse = false;
        q.add(root);
        
        while (!q.isEmpty()) {
            newQ = new ArrayList<TreeNode>();
            subSol = new ArrayList<Integer>();
            for (TreeNode node: q) {
                subSol.add(node.val);
                if (node.left != null) {
                    newQ.add(node.left);
                }
                if (node.right != null) {
                    newQ.add(node.right);
                }
            }
            q = newQ;
            if (reverse) {
                Collections.reverse(subSol);
                reverse = false;
            } else {
                reverse = true;
            }
            sol.add(subSol);
        }
        return sol;
    }
}
