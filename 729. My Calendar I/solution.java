class MyCalendar {
    private List<int[]> events;
    public MyCalendar() {
        events = new ArrayList<int[]>();
    }
    
    public boolean book(int start, int end) {
        for (int[] event: events) {
            if (start < event[1] && end > event[0]) {
                return false;
            }
        }
        events.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
