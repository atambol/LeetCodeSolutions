/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        boolean[] isCommoner = new boolean[n];
        int knownByCount;
        for (int i = 0; i < n; i++) {
            if (isCommoner[i])
                continue;
            
            knownByCount = 0;
            for (int j = 0; j < n; j++) {     
                if (i == j)
                    continue;
                
                if (knows(i, j)) {
                    isCommoner[i] = true;
                }
                
                if (isCommoner[i])
                    continue;
                
                if (knows(j, i)) {
                    isCommoner[j] = true;
                    knownByCount++;
                }
            }
            
            if (knownByCount == n-1 && !isCommoner[i])
                return i;
        }
        
        return -1;
    }
}
