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
    public void recoverTree(TreeNode root) {
        TreeNode[] buffer = new TreeNode[2];
        buffer[0] = null;
        buffer[1] = null;
        
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode prev = null;
        TreeNode node = root;
        
        // inorder traversal to find the non increasing order
        while (node != null || !stack.isEmpty()) {
            if (node != null) {
                stack.add(node);
                node = node.left;
            } else {
                node = stack.pop();
                if (node == null) {
                    continue;
                }
                
                if (prev != null && prev.val > node.val) {
                    if (buffer[0] == null) {
                        buffer[0] = prev;
                    }
                    buffer[1] = node;
                }
                
                prev = node;
                node = node.right;
            }
        }
        
        int tmp;
        tmp = buffer[0].val;
        buffer[0].val = buffer[1].val;
        buffer[1].val = tmp;
    }
}
