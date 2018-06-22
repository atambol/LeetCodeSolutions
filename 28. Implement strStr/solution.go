func strStr(haystack string, needle string) int {
    if haystack == needle {
        return 0
    }
    if len(haystack) == 0 {
        return -1
    }
    if len(needle) == 0 {
        return 0
    }
    if len(needle) > len(haystack) {
        return -1
    }
    
    for i:=0; i<len(haystack) - len(needle) + 1; i++ {
        if haystack[i] == needle[0] {
            match := true
            pos := i
            
            for j:=1; j<len(needle); j++ {
                if needle[j] != haystack[i+j] {
                    match = false
                    break
                } 
            }
            
            if match == true {
                return pos
            } 
        }
    }
    return -1
}
