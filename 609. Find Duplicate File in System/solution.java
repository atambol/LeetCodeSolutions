class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> map = new HashMap<>();
        List<List<String>> sol = new ArrayList<>();
        for (String path: paths) {
            parseAndAdd(path, map);
        }
        
        for (List<String> duplicate : map.values()) {
            if (duplicate.size() > 1) {
                sol.add(duplicate);
            }
        }
        
        return sol;
    }
        
    public void parseAndAdd(String str, Map<String, List<String>> map) {
        List<String> duplicate;
        
        int i = 0;
        int j = 0;
        String parentDir;
        String fileName;
        String content;
        
        // set parent dir
        while (str.charAt(j) != ' ') {
            j++;
        }
        parentDir = str.substring(i, j);
        i = j+1;
        j++;
        
        while (j < str.length()) {
            // set file name
            while (str.charAt(j) != '(') {
                j++;
            } 
            fileName = str.substring(i, j);
            i = j+1;
            j++;
            
            // set content
            while (str.charAt(j) != ')') {
                j++;
            }
            content = str.substring(i, j);
            
            // add to map
            duplicate = map.getOrDefault(content, new ArrayList<>());
            duplicate.add(parentDir + "/" + fileName);
            map.put(content, duplicate);
            
            // update pointers
            j += 2;
            i = j;
        }
    }
}
