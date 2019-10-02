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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode node = root;
        while (k > 0 && (node != null || !stack.isEmpty())) {
            if (node != null) {
                stack.add(node);
                node = node.left;
            } else {
                while (node == null) {
                    node = stack.pop();
                }
                
                k--;
                if (k == 0) {
                    return node.val;
                } else {
                    node = node.right;
                }
            }       
        }
        return -1;
    }
}
