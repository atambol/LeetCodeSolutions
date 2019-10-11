class Solution {
    public int[] dailyTemperatures(int[] T) {
        Stack<Integer> stack = new Stack<Integer>();
        int n = T.length;
        int[] sol = new int[n];

        n--;
        while (n >= 0) {
            while (!stack.isEmpty() && T[stack.peek()] <= T[n]) {
                stack.pop();
            }
            
            if (!stack.isEmpty())
                sol[n] = stack.peek() - n;
            else 
                sol[n] = 0;
            
            stack.add(n);
            n--;
        }
        return sol;
    }
}
