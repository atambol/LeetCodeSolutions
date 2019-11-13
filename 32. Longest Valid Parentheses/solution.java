class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        int size = 0;
        LinkedList<Integer> stack = new LinkedList<>();
        stack.push(-1);
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == ')' && stack.size() > 1 && s.charAt(stack.peek()) == '(') {
                stack.pop();
                size = Math.max(size, i - stack.peek());
            } else {
                stack.push(i);
            }
        }
        return size;
    }
}
