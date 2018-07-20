func isIsomorphic(s string, t string) bool {
    trackerS := make(map[byte]byte)
    trackerT := make(map[byte]byte)
    for i:=0; i<len(s); i++ {
        charS, okS := trackerS[s[i]]
        charT, okT := trackerT[t[i]]
        if !okS && !okT {
            trackerS[s[i]] = t[i]
            trackerT[t[i]] = s[i]
        } else if okS && okT {
            if charS == t[i] && charT == s[i] {
                continue
            } else {
                return false
            }
        } else {
            return false
        }
    }
    return true
}
