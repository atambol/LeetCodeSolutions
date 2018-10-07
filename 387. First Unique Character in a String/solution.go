func firstUniqChar(s string) int {
    count := make([]int, 26, 26)
    for i:=0; i<len(s); i++ {
        index := s[i] - 'a'
        count[index]++
    }
    for i:=0;i<len(s); i++ {
        index := s[i] - 'a'
        if count[index] == 1 {
            return i
        }
    }
    return -1
}
