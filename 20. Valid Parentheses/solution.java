class Solution {
    private static Map<String, String> map = new HashMap<>();
    public Solution() {
        map.put("{", "}");
        map.put("[", "]");
        map.put("(", ")");
    }
    
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();
        String str;
        char c;
        String opening = "{([";
        String closing = "})]";
        for(int i=0; i < s.length(); i++) {
            c = s.charAt(i);
            str = Character.toString(c);
            if (opening.contains(str)) {
                stack.push(str);
            }
            else if (closing.contains(str)) {
                if (stack.size() == 0) {
                    return false;
                }
                String top = stack.pop();
                if (!str.equals(map.get(top))) {
                    return false;
                }
            }
        }
        if (stack.size() > 0) {
            return false;
        }
        return true;
    }
}
