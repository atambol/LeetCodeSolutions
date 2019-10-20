class Solution {
    public int totalFruit(int[] tree) {
        // edge cases
        int n = tree.length;
        if (n < 3) {
            return n;
        }

        // maintain a basket set for each window
        HashSet<Integer> basket = new HashSet<Integer>();
        int prevFruit = -1;
        int prevFruitCount = 0;
        int count = 0;
        int maxCount = 0;
        int fruit;
        for (int i = 0; i < n; i++) {
            fruit = tree[i];
            if (basket.contains(fruit)) {
                count++;
                if (prevFruit != fruit) {
                    prevFruitCount = 0;
                    prevFruit = fruit;
                } 
                prevFruitCount++;
            } else {
                maxCount = Math.max(maxCount, count);
                if (basket.size() == 2) {
                    basket.clear();
                    basket.add(prevFruit);
                } 
                basket.add(fruit);
                count = prevFruitCount + 1;
                prevFruit = fruit;
                prevFruitCount = 1;
            }
        }
        maxCount = Math.max(maxCount, count);
        return maxCount;
    }
}
