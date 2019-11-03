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
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> allLeaves = new ArrayList<List<Integer>>();
        if (root == null) {
            return allLeaves;
        }
        
        // know parent
        Map<TreeNode, TreeNode> parentMap = new HashMap<TreeNode, TreeNode>();
        TreeNode parent;
        List<TreeNode> leafNodes = knowParentAndGetLeaves(parentMap, root);
        List<TreeNode> aux = new ArrayList<TreeNode>();
        List<TreeNode> tmp;
        while (!leafNodes.isEmpty()) {
            List<Integer> leaves = new ArrayList<Integer>();
            for (TreeNode node: leafNodes) {
                leaves.add(node.val);
                parent = parentMap.get(node);
                if (parent != null) {
                    if (parent.left == node) {
                        parent.left = null;
                    } else {
                        parent.right = null;
                    }
                    if (parent.left == null && parent.right == null) {
                        aux.add(parent);
                    }
                }
            }
            
            leafNodes.clear();
            tmp = leafNodes;
            leafNodes = aux;
            aux = tmp;
            allLeaves.add(leaves);
        }
        return allLeaves;
    }
    
    public List<TreeNode> knowParentAndGetLeaves(Map<TreeNode, TreeNode> parentMap, TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<TreeNode> leaves = new ArrayList<TreeNode>(); 
        parentMap.put(root, null);
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                if (root.left != null) {
                    parentMap.put(root.left, root);
                    stack.add(root.left);
                }
                if (root.right != null) {
                    parentMap.put(root.right, root);
                    stack.add(root.right);
                }
                
                if (root.left == null && root.right == null) {
                    leaves.add(root);
                }
                
                root = null;
            } else {
                root = stack.pop();
            }
        }
        return leaves;
    }
}
