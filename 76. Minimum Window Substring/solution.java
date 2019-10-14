class Solution {
    public String minWindow(String s, String t) {
        // edge cases
        if (t.length() == 0 || s.length() == 0 || t.length() > s.length()) {
            return new String("");
        }
        
        if (t.equals(s)) {
            return t;
        }
        
        // init
        Count count = new Count(t);
        int i = 0;
        int j = 0;
        
        // get at least first window
        while (!count.isSafeState() && j < s.length()) {
            count.add(s.charAt(j));
            j++;
        }
        
        if (!count.isSafeState() && j == s.length()) {
            return new String("");
        }
        
        // move window tail
        while (count.isSafeToRemove(s.charAt(i))) {
            count.remove(s.charAt(i));
            i++;
        }
        
        int minI = i;
        int minJ = j;
        
        // keep the window moving
        while (j < s.length()) {
            // move window head
            count.add(s.charAt(j));
            j++;
                            
            // move window tail
            while (count.isSafeToRemove(s.charAt(i))) {
                count.remove(s.charAt(i));
                i++;
            }

            // check if the window is minimum
            if (j - i < minJ - minI) {
                minJ = j;
                minI = i;
            }
        }
        
        return s.substring(minI, minJ);
    }
    
    class Count {
        Map<Character, Integer> currentCount;
        Map<Character, Integer> reqCount;
        
        public Count(String t) {
            currentCount = new HashMap<Character, Integer>();
            reqCount = new HashMap<Character, Integer>();

            char c;
            int count;
            for(int i = 0; i < t.length(); i++) {
                c = t.charAt(i);
                if (reqCount.containsKey(c)) {
                    count = reqCount.get(c);
                    reqCount.put(c, count+1);
                } else {
                    reqCount.put(c, 1);
                    currentCount.put(c, 0);
                }
            }
        }
        
        private boolean isCharImp(char c) {
            return reqCount.containsKey(c);
        }
        
        public void add(char c) {
            if (this.isCharImp(c)) {
                int count = currentCount.get(c);
                currentCount.put(c, count+1);
            }
        }
        
        public void remove(char c) {
            if (this.isCharImp(c)) {
                int count = currentCount.get(c);
                currentCount.put(c, count-1);
            }
        }
        
        public boolean isSafeState() {
            for (char c : reqCount.keySet()) {
                if (reqCount.get(c) > currentCount.get(c)) {
                    return false;
                }
            }
            return true;
        }
        
        public boolean isSafeToRemove(char c) {
            if (!this.isCharImp(c)) {
                return true;
            }
            
            if (currentCount.get(c) - 1 < reqCount.get(c)) {
                return false;
            }
            
            return true;
        }
    }
}
