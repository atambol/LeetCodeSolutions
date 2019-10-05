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
        
        List<String> sol = new ArrayList<String>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                sol.add(String.valueOf(root.val));
                stack.add(root.right);
                root = root.left;
            } else {
                sol.add("#");
                root = stack.pop();
            }
        }
        
        return String.join(",", sol);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) {
            return null;
        }
        
        String[] sol = data.split(",", 0);
        Stack<Result> stack = new Stack<Result>();
        int ptr = 0;
        
        TreeNode root = new TreeNode(Integer.parseInt(sol[ptr]));
        Result r;
        TreeNode node;
        stack.add(new Result(root));
        ptr++;
        while (ptr < sol.length) {
            if (sol[ptr].equals("#")) {
                r = stack.pop();
                if (!r.right) {
                    r.right = true;
                    stack.add(r);
                }
            } else {
                node = new TreeNode(Integer.parseInt(sol[ptr]));
                r = stack.pop();
                if (!r.right) {
                    r.node.left = node;
                    r.right = true;
                    stack.add(r);
                } else {
                    r.node.right = node;
                }
                stack.add(new Result(node));
            }
            ptr++;
        }
        return root;
    }
    
    class Result {
        TreeNode node;
        boolean right;
        
        public Result(TreeNode n) {
            right = false;
            node = n;
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
