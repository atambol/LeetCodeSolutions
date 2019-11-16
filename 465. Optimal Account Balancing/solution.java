class Solution {
    public int minTransfers(int[][] transactions) {
        Map<Integer, Integer> amountMap = new HashMap<Integer, Integer>();
        int lender, ower, amount;
        
        // convert all transactions to amount owed or lent by each
        for (int[] transaction: transactions) {
            lender = transaction[0];
            ower = transaction[1];
            amount = transaction[2];
            amountMap.put(lender, amountMap.getOrDefault(lender, 0) + amount);
            amountMap.put(ower, amountMap.getOrDefault(ower, 0) - amount);
        }
        
        // get all the amounts
        int[] amounts = new int[amountMap.size()];
        int i = 0;
        for (int val: amountMap.values()) {
            amounts[i] = val;
            i++;
        }
        
        // backtrack to get the minimum number of transfers
        return backtrack(amounts, 0);
    }
    
    public int backtrack(int[] amounts, int id) {
        // override when no amount is owed or lent
        while (id < amounts.length && amounts[id] == 0)
            id++;
        
        // base case
        if (id == amounts.length)
            return 0;
        
        // recurse
        int minTransaction = Integer.MAX_VALUE;

        for (int i = id + 1; i < amounts.length; i++) {
            if (amounts[i] * amounts[id] < 0) {
                amounts[i] += amounts[id];
                minTransaction = Math.min(minTransaction, 1 + backtrack(amounts, id+1));
                amounts[i] -= amounts[id];
            }
        }
        return minTransaction;
    }
}
