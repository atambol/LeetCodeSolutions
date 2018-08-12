/**
 * Definition for an interval.
 * type Interval struct {
 *	   Start int
 *	   End   int
 * }
 */
func merge(intervals []Interval) []Interval {
    
    if len(intervals) == 0 {
        return intervals
    }
    
    intervals = mySort(intervals)
    fmt.Println(intervals)

    var sol []Interval

    for i:=0; i<len(intervals); i++ {
        inserted := false
        for j := 0; j<len(sol); j++ {
            if intervals[i].Start >= sol[j].Start && intervals[i].End <= sol[j].End {
                inserted = true
                break
            } else if intervals[i].Start >= sol[j].Start && intervals[i].End >= sol[j].End && intervals[i].Start <= sol[j].End {
                sol[j].End = intervals[i].End
                inserted = true
                break
            } else if intervals[i].Start <= sol[j].Start && intervals[i].End <= sol[j].End && sol[j].Start <= intervals[i].End {
                sol[j].Start = intervals[i].Start
                inserted = true
                break
            }
        }
        
        if inserted == false {
            sol = append(sol, intervals[i])
        }
    }
    
    return sol
}

func mySort(intervals []Interval) []Interval{
    var sorted []Interval
    for i := 0; i < len(intervals); i++ {
        added := false
        for j := 0; j< len(sorted); j++ {
            if intervals[i].Start < sorted[j].Start {
                sorted = append(sorted[:j], append([]Interval{intervals[i]}, sorted[j:]...)...) 
                added = true
                break
            }
        }
        if ! added {
            sorted = append(sorted, intervals[i])
        }

    }
    return sorted
}
