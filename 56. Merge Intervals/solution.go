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
    
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i].Start < intervals[j].Start
    })
    // fmt.Println(intervals)

    var sol []Interval

    for i:=0; i<len(intervals); i++ {
        inserted := false
        for j := 0; j<len(sol); j++ {
            if intervals[i].Start >= sol[j].Start {
                if intervals[i].End <= sol[j].End {
                    inserted = true
                    break
                } else if intervals[i].End >= sol[j].End && intervals[i].Start <= sol[j].End {
                    sol[j].End = intervals[i].End
                    inserted = true
                    break
                }
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
