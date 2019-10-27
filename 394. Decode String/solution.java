class Solution {
    public String decodeString(String s) {
        /***
        The problem consists of parsing string s based on various cases. Parsing is straightforward.
        Storing encoded_string and its corresponding count k is the challenge in this problem.
        We store k and encoded_string in the same str list. k is used as a delimiter as well as multiplier. 
        All the string occurring after a k need to be repeated k times. When extracting from str for 
        concatenation, continue until k is encountered. Then concatenate all the strings extracted and 
        repeat it k times. This way, there is no need to keep track of which encoded_string is associated 
        with which k.
        ***/
        
        // this list will store all the intermediate terms that are extracted as well as their repeat count
        List<String> str = new ArrayList<String>();
        int k;
        String tmp;
        
        int i = 0;
        
        // loop over the string s and handle 4 cases
        while (i < s.length()) {
            // case 1 : ]
            // In this case, extract, concatenate and multiply the strings 
            if (s.charAt(i) == ']') {
                // create a buffer to store all the strings extracted from str until k is encountered or str is empty
                List<String> buffer = new ArrayList<String>();
                while (!str.isEmpty() && !Character.isDigit(str.get(str.size()-1).charAt(0))) {
                    buffer.add(0, str.remove(str.size()-1));
                }
                
                // if k is encountered, extract it and multiply the concatenated strings in buffer by it
                // add it to the str list
                if (!str.isEmpty() && Character.isDigit(str.get(str.size()-1).charAt(0))) {
                    k = Integer.valueOf(str.remove(str.size() - 1));
                    tmp = multiplyString(String.join("", buffer), k);
                    str.add(tmp);
                } 
                // add the concatenated buffer to str list
                else {
                    str.add(String.join("", buffer));
                }
                
                i++;
            } 
            
            // case 2 : [
            else if (s.charAt(i) == '[') {
                i++;
            } 
            
            // case 3 : digits
            // greedily extract as many consecutive digits (k)
            else if (Character.isDigit(s.charAt(i))) {
                StringBuilder num = new StringBuilder();
                while (Character.isDigit(s.charAt(i))) {
                    num.append(Character.toString(s.charAt(i)));
                    i++;
                }
                str.add(num.toString());
            } 
            
            // case 4 : other characters
            // greedily extract as many other characters (encoded_strings)
            else {
                int j = i;
                while (i < s.length() && s.charAt(i) != ']' && s.charAt(i) != '[' && !Character.isDigit(s.charAt(i))) {
                    i++;
                }
                
                str.add(s.substring(j, i));
            }
        }
        
        // Combine all the strings on the same level
        return String.join("", str);
    }

    public String multiplyString(String s, int c) {
        StringBuilder sol = new StringBuilder(); 
        for (int i = 0; i < c; i++) {
            sol.append(s);
        }
        return sol.toString();
    }
}
