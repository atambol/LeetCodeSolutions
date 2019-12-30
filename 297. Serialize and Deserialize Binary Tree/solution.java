/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    private String none = "#";
    private String separator = ",";
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return new String("");
        }
        
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = root;
        List<String> sol = new ArrayList<>();
        while (!stack.isEmpty() || node != null) {
            if (node != null) {
                sol.add(Integer.toString(node.val));
                stack.add(node.right);
                node = node.left;
            } else {
                sol.add(none);
                node = stack.pop();
            }
        }
        
        return String.join(separator, sol);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) {
            return null;
        }
        
        String[] sol = data.split(separator);
        TreeNode root = new TreeNode(Integer.parseInt(sol[0]));
        Node node = new Node(root, false);a
        Stack<Node> stack = new Stack<>();
        stack.add(node);
        for (int i = 1; i < sol.length; i++) {
            String s = sol[i];
            if (s.equals(none)) {
                node = stack.peek();
                if (node.isLeftDone) {
                    stack.pop(); 
                } else {
                    node.isLeftDone = true;
                }
            } else {
                node = stack.peek();
                if (node.isLeftDone) {
                    node.treeNode.right = new TreeNode(Integer.parseInt(s));
                    stack.pop();
                    stack.add(new Node(node.treeNode.right, false));
                } else {
                    node.treeNode.left = new TreeNode(Integer.parseInt(s));
                    stack.add(new Node(node.treeNode.left, false));
                    node.isLeftDone = true;
                }
            }
        }
        
        return root;
    }
    
    public class Node {
        public TreeNode treeNode;
        public boolean isLeftDone;
        
        public Node(TreeNode t, boolean i) {
            treeNode = t;
            isLeftDone = i;
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
