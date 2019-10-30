class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] i1, int[] i2) {
                if (i2[0] == i1[0]) {
                    return i1[1] - i2[1];
                }
                return i1[0] - i2[0];
            }
        });
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int count = 0;
        
        for (int i = 0; i < intervals.length; i++) {
            while (!heap.isEmpty() && heap.peek() <= intervals[i][0]) {
                heap.poll();
            }
            
            heap.add(intervals[i][1]);
            count = Math.max(count, heap.size());
        }
        return count;
    }
}
