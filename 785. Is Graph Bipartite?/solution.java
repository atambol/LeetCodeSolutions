class Solution {
    private int white = 0;
    private int blue = 1;
    private int red = 2;
    
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length];
        Stack<Integer> stack = new Stack<>();
        int oppColor;
        for (int root = 0; root < graph.length; root++) {
            if (color[root] == white) {
                stack.add(root);
                color[root] = blue;
                while (!stack.isEmpty()) {
                    root = stack.pop();
                    oppColor = color[root] == blue?red:blue;
                    for (int vertex: graph[root]) {
                        if (color[vertex] == white) {
                            color[vertex] = oppColor;
                            stack.add(vertex);
                        } else {
                            if (color[vertex] != oppColor) {
                                return false;
                            } else {
                                ;;
                            }
                        }
                    }
                }
            }
        }
        
        return true;
    }
}
