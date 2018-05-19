func lengthOfLongestSubstring(s string) int {
    prevSubStringLength := 0
    newSubString := make(map[rune]int)
    for i, char := range s {
        if j, ok := newSubString[char]; ok {
            if prevSubStringLength < len(newSubString) {
                prevSubStringLength = len(newSubString)
            }
            for k, v := range newSubString {
                if v <= j {
                    delete(newSubString, k)
                }
            }
        }
        newSubString[char] = i
    }

    if prevSubStringLength < len(newSubString) {
        prevSubStringLength = len(newSubString)
    }
    return prevSubStringLength
}
