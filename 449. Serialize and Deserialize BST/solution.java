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

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return new String("");
        }
        
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<String> sol = new ArrayList<String>();
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                sol.add(String.valueOf(root.val));
                stack.push(root.right);
                root = root.left;
            } else {
                while (!stack.isEmpty() && root == null) {
                    root = stack.pop();
                }
            }
        }
        
        return String.join(",", sol);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) {
            return null;
        }
        
        List<String> sol = new ArrayList<String>(Arrays.asList(data.split(",")));
        Collections.reverse(sol);
        TreeNode root = new TreeNode(Integer.parseInt(sol.remove(sol.size()-1)));
        TreeNode node, parent;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        while (sol.size() > 0) {
            node = new TreeNode(Integer.parseInt(sol.remove(sol.size()-1)));
            parent = stack.pop();
            if (parent.val > node.val) {
                parent.left = node;
                stack.push(parent);
            } else {
                while (!stack.isEmpty() && stack.peek().val < node.val) {
                    parent = stack.pop();
                }
                parent.right = node;
            }
            stack.push(node);
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
