/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
 // O(n + n/2 + n/4 ..) = O(n) time complexity, O(n) space complexity
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> allLeaves = new ArrayList<List<Integer>>();
        if (root == null) {
            return allLeaves;
        }
        
        while (root.left != null || root.right != null) {
            allLeaves.add(extractLeaves(root));
        }
        
        allLeaves.add(new ArrayList<Integer>(Arrays.asList(root.val)));
        return allLeaves;
    }
    
    public List<Integer> extractLeaves(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> leaves = new ArrayList<Integer>(); 
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                if (root.left != null && root.left.left == null && root.left.right == null) {
                    leaves.add(root.left.val);
                    root.left = null;
                } else {
                    stack.add(root.left);
                }
                
                if (root.right != null && root.right.left == null && root.right.right == null) {
                    leaves.add(root.right.val);
                    root.right = null;
                } else {
                    stack.add(root.right);
                }
                
                root = null;
            } else {
                root = stack.pop();
            }
        }
        return leaves;
    }
}
