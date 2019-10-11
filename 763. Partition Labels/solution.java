class Solution {
    public List<Integer> partitionLabels(String S) {
        int[] starts = new int[26];
        int[] ends = new int[26];
        
        // get start and end position
        for (int i = 0; i < 26; i++) {
            starts[i] = -1;
            ends[i] = -1;
        }
        
        int pos;
        for (int i = 0; i < S.length(); i++) {
            pos = Character.getNumericValue(S.charAt(i))-Character.getNumericValue('a');
            if (starts[pos] == -1) {
                starts[pos] = i;
            }
            ends[pos] = i;
        }
        
        // convert to merge interval problem
        List<int[]> intervals = new ArrayList<int[]>();
        for(int i = 0; i < 26; i++) {
            if (starts[i] != -1) {
                intervals.add(new int[]{starts[i], ends[i]});
            }
        }
        
        // merge intervals
        Collections.sort(intervals, (a, b) -> a[0] - b[0]);
        int start, end;
        List <Integer> sol = new ArrayList<Integer>();
        start = intervals.get(0)[0];
        end = intervals.get(0)[1];
        int i = 1;
        while (i < intervals.size()) {
            if (intervals.get(i)[0] <= end) {
                end = Math.max(intervals.get(i)[1], end);
            } else {
                sol.add(end - start + 1);
                start = intervals.get(i)[0];
                end = intervals.get(i)[1];
            }
            i++;
        }
        
        sol.add(end - start + 1);
        
        return sol;
    }
}
