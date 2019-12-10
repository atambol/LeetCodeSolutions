/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/
class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        // add to heap
        PriorityQueue<Interval> heap = new PriorityQueue<>((a,b) -> a.start!=b.start?a.start-b.start:a.end-b.end);
        for (List<Interval> s: schedule) {
            for (Interval i: s) {
                heap.add(i);
            }
        }
        
        // find sol
        List<Interval> sol = new ArrayList<>();
        Interval prev = heap.poll();
        Interval cur;
        while (!heap.isEmpty()) {
            cur = heap.poll();
            if (cur.start > prev.end) {
                sol.add(new Interval(prev.end, cur.start));
                prev = cur;
            } else {
                prev.end = Math.max(prev.end, cur.end);
            }
        }
        
        return sol;
    }
}
