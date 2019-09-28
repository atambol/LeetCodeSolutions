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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> sol = new ArrayList<Integer>();
        Stack<Traversal> stack = new Stack<Traversal>();
        TreeNode node = root;
        Traversal traversal;
        while (node != null || !stack.isEmpty()) {
            if (node != null) {
                traversal = new Traversal(node);
                stack.add(traversal);
                node = node.left;
            } else {
                traversal = stack.pop();
                if (traversal.isRightVisited()) {
                    sol.add(traversal.node.val);
                    node = null;
                } else {
                    node = traversal.node.right;
                    traversal.setRightVisited();
                    stack.add(traversal);
                }
            }
        }
        return sol;
    }
    
    class Traversal {        
        private TreeNode node;
        private boolean rightVisited;
        
        public Traversal(TreeNode node) {
            this.node = node;
            boolean rightVisited = false;
        }
        
        public boolean isRightVisited() {
            return rightVisited;
        }
        
        public void setRightVisited() {
            rightVisited = true;
        }
    }
}
