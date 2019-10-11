class MyCalendarTwo {
    List<int[]> events;
    List<int[]> doubleBookings;
    
    public MyCalendarTwo() {
        events = new ArrayList<int[]>();
        doubleBookings = new ArrayList<int[]>();
    }
    
    public boolean book(int start, int end) {
        // check if triple booking is going to happen
        for (int[] doubleBooking: doubleBookings) {
            if (start < doubleBooking[1] && doubleBooking[0] < end) {
                return false;
            }
        }
        
        // insert the event
        for (int[] event: events) {
            if (start < event[1] && event[0] < end) {
                doubleBookings.add(new int[]{Math.max(start, event[0]), Math.min(end, event[1])});
            }
        }
        events.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */
