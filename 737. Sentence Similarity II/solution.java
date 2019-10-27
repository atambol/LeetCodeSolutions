class Solution {
    class DSD {
        private HashMap<String, String> parents;
        private HashMap<String, HashSet<String>> children;
        
        public DSD() {
            parents = new HashMap<String, String>();
            children = new HashMap<String, HashSet<String>>();
        }
        
        public boolean hasKey(String s) {
            return parents.containsKey(s);
        }
        
        public void makeSet(String s) {
            parents.put(s, s);
            HashSet<String> c = new HashSet<String>();
            c.add(s);
            children.put(s, c);
        }
        
        public String find(String s) {
            return parents.get(s);
        }
        
        public void union(String s, String t) {
            String p1 = find(s);
            String p2 = find(t);
            
            if (p1.equals(p2)) {
                return;
            }
            
            if (children.get(p1).size() > children.get(p2).size()) {
                update(p1, p2);
            } else {
                update(p2, p1);
            }
        }
        
        public void update(String s, String t) {
            HashSet<String> cs = children.get(s);
            HashSet<String> ct = children.get(t);
            
            for (String c: ct) {
                parents.put(c, s);
                cs.add(c);
            }
            
            parents.put(t, s);
            cs.add(t);
            ct.clear();
        }
        
        // public void print() {
        //     // Parents
        //     for (String p: parents.keySet()) {
        //         System.out.printf("%s \n", p);
        //         for (String c: children.get(p)) {
        //             System.out.printf("\t%s \n", c);
        //         }
        //     }
        // }
    }
    
    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, List<List<String>> pairs) {
        if (words1.length != words2.length) {
            return false;
        }
        
        DSD dsd = new DSD();
        
        String s1, s2;
        String p1, p2;
        for (List<String> pair: pairs) {
            s1 = pair.get(0);
            s2 = pair.get(1);
            
            if (!dsd.hasKey(s1)) {
                dsd.makeSet(s1);
            }
            
            if (!dsd.hasKey(s2)) {
                dsd.makeSet(s2);
            }
            
            dsd.union(s1, s2);
        }
        
        // dsd.print();
        for (int i = 0; i < words1.length; i++) {
            s1 = words1[i];
            s2 = words2[i];
            if (s1.equals(s2)) {
                continue;
            }
            
            if (!dsd.hasKey(s1) || !dsd.hasKey(s2)) {
                // System.out.printf("key not present %s, %s", s1, s2);
                return false;
            }
            
            p1 = dsd.find(s1);
            p2 = dsd.find(s2);
            if (!p1.equals(p2)) {
                // System.out.printf("not same parent %s, %s", s1, s2);
                return false;
            }
        }

        return true;
    }
}
