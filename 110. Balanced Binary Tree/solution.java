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
    public boolean isBalanced(TreeNode root) {
        Results result = checkBalanced(root);
        return result.getBalance();
    }
    
    public Results checkBalanced(TreeNode root) {
        Results results = new Results();
        
        if (root == null) {
            return results;
        }
        
        else if (root.left != null && root.right == null) {
            Results left = checkBalanced(root.left);
            results.setHeight(left.getHeight() + 1);
            results.setBalance(left.getBalance() && left.getHeight() <= 1);
            return results;
        } 
        
        else if (root.left == null && root.right != null) {
            Results right = checkBalanced(root.right);
            results.setHeight(right.getHeight() + 1);
            results.setBalance(right.getBalance() && right.getHeight() <= 1);
            return results;
        }
        
        else {
            Results left = checkBalanced(root.left);
            Results right = checkBalanced(root.right);
            
            results.setHeight(Math.max(right.getHeight(), left.getHeight()) + 1);
            results.setBalance(left.getBalance() &&
                               right.getBalance() &&
                               Math.abs(left.getHeight() - right.getHeight()) <= 1);
            return results;
        }
    }
    
    class Results {
        private boolean balance;
        private int height;
        
        public Results() {
            height = 0;
            balance = true;
        }
        
        public void setBalance(boolean balance) {
            this.balance = balance;
        }
        
        public boolean getBalance() {
            return balance;
        }
        
        public void setHeight(int height) {
            this.height = height;
        }
        
        public int getHeight() {
            return height;
        }
        
    }
}
