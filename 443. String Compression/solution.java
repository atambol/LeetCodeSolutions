class Solution {
    public int compress(char[] chars) {
        int start = 0, end = 0, writeHead = 0;
        
        while (end < chars.length) {
            if (chars[start] == chars[end]) {
                end++;
            } else {
                chars[writeHead] = chars[start];
                writeHead++;
                if (end - start > 1) {
                    String count = Integer.toString(end - start);
                    for (int i = 0; i < count.length(); i++) {
                        chars[writeHead++] = count.charAt(i);
                    }
                }
                start = end;
                end++;
            }
        }
        chars[writeHead] = chars[start];
        writeHead++;
        if (end - start > 1) {
            String count = Integer.toString(end - start);
            for (int i = 0; i < count.length(); i++) {
                chars[writeHead++] = count.charAt(i);
            }
        }
        return writeHead;
    }
}
