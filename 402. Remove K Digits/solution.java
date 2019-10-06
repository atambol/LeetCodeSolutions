class Solution {
    public String removeKdigits(String num, int k) {
        // edge cases
        if (num.length() <= k) {
            return new String("0");
        }
        
        // convert to a list
        List<Integer> list = new ArrayList<Integer>(num.length());
        for (int i = 0; i < num.length(); i++) {
            list.add(Character.getNumericValue(num.charAt(i)));
        }
        
        int i = 1;
        while (i < list.size() && k > 0) {
            if (i > 0 && list.get(i-1) > list.get(i)) {
                list.remove(i-1);
                k--;
                i--;
            }
            else  
                i++;
        }
        
        // remove any remaining numbers from left
        while (k > 0) {
            list.remove(list.size()-1);
            k--;
        }
        
        // check for any leading 0s
        i = 0;
        while (i < list.size()) {
            if (i == 0 && list.get(i) == 0) {
                list.remove(i);
                i--;
            }
            i++;
        }
        if (list.size() == 0) {
            return new String("0");
        } 
        
        // convert list to String
        StringBuilder sb = new StringBuilder();
        for (i = 0; i < list.size(); i++) {
            sb.append(String.valueOf(list.get(i)));
        }
        return sb.toString();
    }
}
