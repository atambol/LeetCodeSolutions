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
    public int largestBSTSubtree(TreeNode root) {
        SubTree subTree = helper(root);
        return subTree.count;
    }
    
    public SubTree helper(TreeNode root) {
        SubTree left, right, subTree;
        if (root == null) {
            return new SubTree(0, -1, -1, true);
        }
        

        left = helper(root.left);
        right = helper(root.right);
        int min = (left.min == -1) ? root.val : left.min;
        int max = (right.max == -1) ? root.val : right.max;
        if ((root.left == null || root.val > left.max) && 
            (root.right == null || root.val < right.min) && 
            left.isBST && right.isBST) {
            return new SubTree(left.count + right.count + 1, min, max, true);
        } else {
            return new SubTree(Math.max(left.count, right.count), min, max, false);
        }
    }
    
    public class SubTree {
        public int count;
        public boolean isBST;
        public int min;
        public int max;
        
        public SubTree(int count, int min, int max, boolean isBST) {
            this.count = count;
            this.min = min;
            this.max = max;
            this.isBST = isBST;
        }
    }
}
