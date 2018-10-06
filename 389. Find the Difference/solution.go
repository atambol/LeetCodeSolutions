func findTheDifference(s string, t string) byte {
    rec := make([]int, 26, 26)
    for _, r := range s {
        i := getIndex(r)
        rec[i]++
    }
    
    index := -1
    for _, r := range t {
        i := getIndex(r)
        rec[i]--
        if rec[i] < 0 {
            index = i
            break
        }
    }
    
    return byte(rune(index+97))
}

func getIndex(r rune) int {
    return int(r) - 97
}
