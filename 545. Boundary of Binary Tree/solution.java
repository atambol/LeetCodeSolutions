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
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> sol = new ArrayList<Integer>();
        if (root == null) {
            return sol;
        }
        sol.add(root.val);
        
        // left
        TreeNode node = root.left;
        while (node != null) {
            sol.add(node.val);
            if (node.left != null) 
                node = node.left;
            else
                node = node.right;
        }

        if (sol.size() > 1) 
            sol.remove(sol.size()-1);
        
        // bottom
        Stack<TreeNode> stack = new Stack<TreeNode>();
        node = root.left;
        stack.add(root.right);
        while (node != null || !stack.isEmpty()) {
            if (node != null) {
                if (node.left == null && node.right == null) {
                    sol.add(node.val);
                    node = null;
                } else {
                    stack.add(node.right);
                    node = node.left;
                }
            } else {
                node = stack.pop();
            }
        }
        
        // right
        List<Integer> aux = new ArrayList<Integer>();
        node = root.right;
        while (node != null) {
            aux.add(node.val);
            if (node.right != null) 
                node = node.right;
            else
                node = node.left;
        }

        if (aux.size() > 0)
            aux.remove(aux.size()-1);
        
        Collections.reverse(aux);
        sol.addAll(aux);
        
        return sol;
    }
}
