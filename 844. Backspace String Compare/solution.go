func backspaceCompare(S string, T string) bool {
    s := len(S) -1
    t := len(T) -1
    sCount := 0
    tCount := 0
    for s >= 0 || t >= 0 {
        if s >= 0 && S[s] == '#' {
            sCount++
            s--
            continue
        }
        
        if t >= 0 && T[t] == '#' {
            tCount++
            t--
            continue
        }
        
        if s >= 0 && sCount > 0 {
            s--
            sCount--
            continue
        }
        
        if t >= 0 && tCount > 0 {
            t--
            tCount--
            continue
        }
        
        if s < 0 || t < 0 {
            return false
        }
        
        if S[s] != T[t] {
            return false
        } else {
            s--
            t--
        }
    }
    
    return true
}
