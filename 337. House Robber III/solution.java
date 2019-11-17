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
    public int rob(TreeNode root) {
        if (root == null)
            return 0;
        
        int[] sol = myRob(root);
        return Math.max(sol[0], sol[1]);
    }
    
    public int[] myRob(TreeNode root) {
        int[] sol = new int[]{0, 0};
        if (root == null)
            return sol;
        
        int[] leftSol = myRob(root.left);
        int[] rightSol = myRob(root.right);
        
        sol[0] = leftSol[1] + rightSol[1] + root.val;
        sol[1] = Math.max(leftSol[0], leftSol[1]) + Math.max(rightSol[1], rightSol[0]);
        return sol;
    }
}
