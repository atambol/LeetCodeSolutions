class Solution {
    private Map<String, List<String>> map;
    
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return new ArrayList<String>();
        }
        map = new HashMap<>();
        map.put("2", Arrays.asList("a", "b", "c"));
        map.put("3", Arrays.asList("d", "e", "f"));
        map.put("4", Arrays.asList("g", "h", "i"));
        map.put("5", Arrays.asList("j", "k", "l"));
        map.put("6", Arrays.asList("m", "n", "o"));
        map.put("7", Arrays.asList("p", "q", "r", "s"));
        map.put("8", Arrays.asList("t", "u", "v"));
        map.put("9", Arrays.asList("w", "x", "y", "z"));
        
        return backtrack(digits);
    }
    
    public List<String> backtrack(String digits) {
        if (digits.length() == 1)
            return map.get(digits.substring(0, 1));
        List<String> sol = new ArrayList<String>();
        List<String> subsol = backtrack(digits.substring(1, digits.length()));
        String cur = digits.substring(0, 1);
        for (String s: subsol)
            for (String c: map.get(cur))
                sol.add(c + s);
        return sol;
    }
}
