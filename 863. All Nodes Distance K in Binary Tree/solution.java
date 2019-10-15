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
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        List<Integer> sol = new ArrayList<Integer>();
        
        // edge case
        if (root == null) {
            return sol;
        }
        
        // convert to graph
        Map<TreeNode, List<TreeNode>> graph = toGraph(root);
        
        // dfs for K dist
        HashSet<TreeNode> visited = new HashSet<TreeNode>();
        dfs(graph, target, K, sol, visited);
        
        return sol;
    }
    
    public void dfs(Map<TreeNode, List<TreeNode>> graph,
                   TreeNode target,
                   int K,
                   List<Integer> sol,
                   HashSet<TreeNode> visited) {    
        if (target == null) {
            return;
        }
        if (K == 0) {
            sol.add(target.val);
            return;
        }
        
        visited.add(target);
        List<TreeNode> adjList = graph.get(target);
        for(TreeNode node: adjList) {
            if (!visited.contains(node)) {
                dfs(graph, node, K-1, sol, visited);
            }
        }
        
        visited.remove(target);
    }
    
    public Map<TreeNode, List<TreeNode>> toGraph(TreeNode root) {
        Map<TreeNode, List<TreeNode>> graph = new HashMap<TreeNode, List<TreeNode>>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode node = root;
        
        List<TreeNode> adjList = new ArrayList<TreeNode>();
        graph.put(root, adjList);
        
        // preorder
        while (node != null || !stack.isEmpty()) {
            if (node != null) {
                if (node.left != null) {
                    adjList = graph.get(node);
                    adjList.add(node.left);
                    adjList = new ArrayList<TreeNode>();
                    adjList.add(node);
                    graph.put(node.left, adjList);
                }
                
                 if (node.right != null) {
                    adjList = graph.get(node);
                    adjList.add(node.right);
                    adjList = new ArrayList<TreeNode>();
                    adjList.add(node);
                    graph.put(node.right, adjList);
                }

                stack.push(node.right);
                node = node.left;
            } else {
                while (node == null && !stack.empty()) {
                    node = stack.pop();
                }
            }
        }
        
        return graph;
    }
}
