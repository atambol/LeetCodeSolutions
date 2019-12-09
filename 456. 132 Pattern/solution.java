class Solution {
    public boolean find132pattern(int[] nums) {
        // edge cases
        int n = nums.length;
        if (n < 3) 
            return false;
        
        // find all the minimum numbers
        int[] mins = new int[n];
        mins[0] = nums[0];
        for (int i = 1; i < n; i++)
            mins[i] = Math.min(mins[i-1], nums[i]);
        
        // start traversing in reverse
        n--;
        Stack<Integer> stack = new Stack<>();
        while (n >= 0) {
            // System.out.println(n);
            while (!stack.isEmpty() && stack.peek() <= mins[n])
                stack.pop();

            if (!stack.isEmpty())
                if (stack.peek() > mins[n] && stack.peek() < nums[n])
                    return true;
                    
            stack.push(nums[n]);
            n--;
        }
        
        return false;
        
    }
}
