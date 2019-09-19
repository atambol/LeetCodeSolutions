class Solution {
    private static final Map<String, String[]> keyMap = Collections.unmodifiableMap(
    new HashMap<String, String[]>() {{
        put("2", new String[] {"a", "b", "c"});
        put("3", new String[] {"d", "e", "f"});
        put("4", new String[] {"g", "h", "i"});
        put("5", new String[] {"j", "k", "l"});
        put("6", new String[] {"m", "n", "o"});
        put("7", new String[] {"p", "q", "r", "s"});
        put("8", new String[] {"t", "u", "v"});
        put("9", new String[] {"w", "x", "y", "z"});
    }});
    
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return new ArrayList<String>();
        }
        return backtrack(0, digits);
    }
    
    public List<String> backtrack(int pos, String digits) {
        List<String> sol = new ArrayList<String>();
        char c = digits.charAt(pos);
        String s = String.valueOf(c);

        // base case
        if (pos == digits.length()-1) {
            for (String key: keyMap.get(s)) {
                String tmp = new String();
                tmp = key;
                sol.add(tmp);
            }
            return sol;
        }
        
        // intermediate case
        List<String> sol_intermediate = backtrack(pos+1, digits);
        for (String key: keyMap.get(s)) {
            for (String suffix: sol_intermediate) {
                 sol.add(key+suffix);
            }
        }
        return sol;
    }
}
