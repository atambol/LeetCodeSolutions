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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        List<TreeNode> roots = new ArrayList<>();
        if (root == null) 
            return roots;
        
        // create toDelete set
        Set<Integer> toDelete = new HashSet<Integer>();
        for (int val: to_delete) {
            toDelete.add(val);
        }
        
        // for dfs
        Stack<Subtree> stack = new Stack<>();
        Subtree subtree = new Subtree(root, true, null);
        stack.add(subtree);
        while (!stack.isEmpty()) {
            subtree = stack.pop();
            if (toDelete.contains(subtree.node.val)) {
                if (subtree.node.left != null)
                    stack.add(new Subtree(subtree.node.left, true, subtree.node));
                
                if (subtree.node.right != null)
                    stack.add(new Subtree(subtree.node.right, true, subtree.node));
                
                subtree.delete();
            } else {
                if (subtree.node.left != null)
                    stack.add(new Subtree(subtree.node.left, false, subtree.node));
                
                if (subtree.node.right != null)
                    stack.add(new Subtree(subtree.node.right, false, subtree.node));
                
                if (subtree.isRoot) {
                    roots.add(subtree.node);
                }
            }
        }
        
        return roots;
    }
    
    class Subtree {
        public TreeNode node;
        public TreeNode prev;
        public boolean isRoot;
        
        public Subtree(TreeNode n, boolean i, TreeNode p) {
            node = n;
            isRoot = i;
            prev = p;
        }
        
        public void delete() {
            if (prev != null) {
                if (prev.left == node) {
                    prev.left = null;
                } else {
                    prev.right = null;
                }
            }
        }
    }
}
