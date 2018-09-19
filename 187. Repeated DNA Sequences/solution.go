func findRepeatedDnaSequences(s string) []string {
    seen := make(map[string]bool)
    repeat := make(map[string]bool)
    for i := 0; i + 10 <= len(s); i++ {
        if _, ok := seen[s[i:i+10]]; ok {
            repeat[s[i:i+10]] = true
        } else {
            seen[s[i:i+10]] = true
        }
    }
    
    res := make([]string, 0, len(repeat))
    for seq := range repeat {
        res = append(res, seq)
    }
    
    return res
}
