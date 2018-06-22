func longestCommonPrefix(strs []string) string {
    // Handle edge cases
    if len(strs) == 1 {
        return strs[0]
    }
    if len(strs) == 0 {
        return ""
    }
    
    // Find the smallest string in the array of strings
    smallestLen := len(strs[0])
    smallestIndex := 0
    for i:=0;i<len(strs);i++ {
        if len(strs[i]) < smallestLen {
            smallestLen = len(strs[i])
            smallestIndex = i
        }
    }
    
    if len(strs[smallestIndex]) == 0 {
        return ""
    }
    
    // Compare the first i elements of the smallest string with every other string
    for i:=smallestLen-1; i>=0; i-- {
        allMatch := true
        for j:=0; j<len(strs); j++ {
            if j == smallestIndex {
                continue
            } else {
                if strs[j][:i+1] != strs[smallestIndex][:i+1] {
                    allMatch = false
                    break
                }
            }
        }
        
        if allMatch == true {
            return strs[smallestIndex][:i+1]
        }
    }
    return ""
}
