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
    public int maxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            Result result = recurse(root);
            return result.maxSum;
        }
    }
    
    public Result recurse(TreeNode root) {
        Result result = new Result(root.val, root.val);
        
        if (root.left == null && root.right == null) {
            ;
        } else if (root.left != null && root.right == null) {
            Result left = recurse(root.left);
            result.maxPath = Math.max(root.val, root.val + left.maxPath);
            result.maxSum = Math.max(result.maxPath, left.maxSum);
        } else if (root.right != null && root.left == null) {
            Result right = recurse(root.right);
            result.maxPath = Math.max(root.val, root.val + right.maxPath);
            result.maxSum = Math.max(result.maxPath, right.maxSum);
        } else {
            Result left = recurse(root.left);
            Result right = recurse(root.right);
            result.maxPath = Math.max(root.val, Math.max(root.val + left.maxPath, root.val + right.maxPath));
            result.maxSum = Math.max(Math.max(result.maxPath, left.maxSum), Math.max(right.maxSum, left.maxPath + root.val + right.maxPath));
        }
        
        return result;
    }
    
    class Result {
        public int maxSum;
        public int maxPath;
        
        public Result(int maxSum, int maxPath) {
            this.maxPath = maxPath;
            this.maxSum = maxSum;
        }
    }
}
