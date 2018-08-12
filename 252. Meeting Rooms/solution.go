func canAttendMeetings(intervals []Interval) bool {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i].Start < intervals[j].Start
    })
    
    for i := 0; i < len(intervals) - 1; i++ {
        if intervals[i].End > intervals[i+1].Start {
            return false
        }
    }
    return true
}
